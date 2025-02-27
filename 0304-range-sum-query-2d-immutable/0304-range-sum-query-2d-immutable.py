class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.res = [[0] * (len(matrix[0])+1) for _ in range((len(matrix)+1))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                self.res[row][col] = matrix[row][col] + self.res[row][col-1]+self.res[row-1][col] - self.res[row-1][col-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.res[row2][col2] - self.res[row2][col1-1] - self.res[row1-1][col2] + self.res[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)