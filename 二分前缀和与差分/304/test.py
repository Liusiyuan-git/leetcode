class NumMatrix:

    def __init__(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        self.sum = [[0] * (m+1) for row in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                self.sum[i][j] = self.sum[i-1][j] + self.sum[i][j-1] - self.sum[i-1][j-1] + matrix[i-1][j-1]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        return self.sum[row2][col2] - self.sum[row2][col1-1] - self.sum[row1-1][col2] + self.sum[row1-1][col1-1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)