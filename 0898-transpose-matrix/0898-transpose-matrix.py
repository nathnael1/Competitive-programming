import numpy as np
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        #creating a matrix to store the transpose matrix
        row_length = len(matrix)
        col_length = len(matrix[0])
        transposed_matrix = [[0]*row_length for _ in range(col_length)]

        #changing the value of row to column and viceversa
        for row_index in range(row_length):
            for col_index in range(col_length):
                transposed_matrix[col_index][row_index] = matrix[row_index][col_index]
        return transposed_matrix
