class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        #maximum rotation is 4 so rotation is less than 4
        temporary_matrix = [[0] * len(mat) for item in range(len(mat))]
        rotation = 0
        while rotation < 4:
            #temporary_matrix to check weather rotation is possible or not
            # temporary_matrix = [[0]*len(mat) for item in range(len(mat))]
        
            #going through each row of matrix
            for row_index in range(len(mat)):

                #going through each col on matrix
                for col_index in range(len(mat[row_index])):
                    
                    #changing the col of temporary matrix to row with shown pattern
                    changed_row = col_index
                    changed_column = len(mat[row_index]) - (row_index + 1)
                    temporary_matrix[changed_row][changed_column] = mat[row_index][col_index]
            print(temporary_matrix,target)
            
            if temporary_matrix == target:
                return True
            mat = temporary_matrix[:]
            temporary_matrix = [[0] * len(mat) for item in range(len(mat))]
            rotation +=1
        return False
        