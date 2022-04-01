class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        f = [[0] * m] * n
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                elif i == 0 and j == 0:
                    f[i][j] = 1
                elif i == 0:
                    f[i][j] = f[i][j - 1]
                elif j == 0:
                    f[i][j] = f[i - 1][j]
                else:
                    f[i][j] = f[i][j - 1] + f[i - 1][j]
        return f[n - 1][m -1]
