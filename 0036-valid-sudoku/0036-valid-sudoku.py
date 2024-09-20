import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      
        row = set()
        for i in range(len(board)):
            for j in board[i]:
                if j != ".":
                    if j in row:
                        return False
                    row.add(j)
            row = set()
        
        board = np.array(board)
        transposed = np.transpose(board)
        row = set()
        for i in range(len(transposed)):
            for j in transposed[i]:
                if j!=".":
                    if j in row:
                        return False
                    row.add(j)
            row = set()

        
        for k in range(9):
            if not self.valid_subgrid(board, k):
                return False

        return True

    def valid_subgrid(self, board: List[List[str]], subgrid_index: int) -> bool:
        subgrid = set()
        row_start = (subgrid_index // 3) * 3
        column_start = (subgrid_index % 3) * 3
        for i in range(3):
            for j in range(3):
                value = board[row_start + i][column_start + j]
                if value != '.':
                    if value in subgrid:
                        return False
                    subgrid.add(value)
        return True

