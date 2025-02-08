class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def horizontal_check(matrix):
            #appending each row in a set
            for i in range(len(matrix)):
                seen = set()
                for j in range(len(matrix[0])):
                    if matrix[i][j] in seen:
                        return False
                    if matrix[i][j] != ".":
                        seen.add(matrix[i][j])
            return True
        
        def vertical_check(matrix):
            #creating transpose
            row_length = len(matrix)
            col_length = len(matrix[0])
            copied_matrix = [[0]*row_length for _ in range(col_length)]
            for i in range(row_length):
                for j in range(col_length):
                    copied_matrix[i][j] = matrix[j][i]

            #calling the horizontal_check
            return horizontal_check(copied_matrix)
        
        def sub_grid_check(matrix):
            
            for row in range(0,9,3):
                for col in range(0,9,3):
                    seen = set()
                    for i in range(3):
                        for j in range(3):
                            if matrix[row+i][col+j] in seen:
                                return False
                            if matrix[row+i][col+j] != ".":
                                seen.add(matrix[row+i][col+j])
            return True
        return horizontal_check(board) and vertical_check(board) and sub_grid_check(board)
                        