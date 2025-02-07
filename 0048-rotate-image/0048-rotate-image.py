class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #first transpose the matrix
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]      

        
        #reverse the matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])//2):
                matrix[i][j], matrix[i][-j-1] =  matrix[i][-j-1], matrix[i][j]
