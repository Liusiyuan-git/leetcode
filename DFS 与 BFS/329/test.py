class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.dist = None
        self.dx = [-1, 0, 0, 1]
        self.dy = [0, -1, 1, 0]
        self.matrix = None

    def longestIncreasingPath(self, matrix) -> int:
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        ans = 0
        self.dist = [[0 for i in range(self.n)] for j in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                ans = max(ans, self.dfs(i, j))
        return ans

    def valid(self, i, j):
        return i >= 0 and i < self.m and j >= 0 and i < self.n

    def dfs(self, x, y):
        if self.dist[x][y] != 0:
            return self.dist[x][y]
        self.dist[x][y] = 1
        for k in range(4):
            nx = x + self.dx[k]
            ny = y + self.dy[k]
            if self.valid(nx, ny) and self.matrix[nx][ny] > self.matrix[x][y]:
                self.dist[x][y] = max(self.dfs(nx, ny) + 1, self.dist[x][y])
        return self.dist[x][y]
s = Solution()
s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])





