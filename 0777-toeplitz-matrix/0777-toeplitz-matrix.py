class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        hashed = set()
        value = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j!=0 and i!=0:
                    if matrix[i][j]!=matrix[i-1][j-1]:
                        return False
        return True
