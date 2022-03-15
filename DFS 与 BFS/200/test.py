class Solution:
    def __init__(self):
        self.m = None
        self.n = None
        self.visited = None

    def numIslands(self, grid) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.visited = [[False for i in range(self.n)] for j in range(self.m)]
        ans = 0
        for i in range(0, self.m):
            for j in range(0, self.n):
                if grid[i][j] != "0" and not self.visited[i][j]:
                    ans += 1
                    self.visited[i][j] = True
                    self.dfs(grid, i, j)
        return ans

    def dfs(self, grid, i, j):
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        queue = [[i, j]]
        while queue:
            x = queue[0][0]
            y = queue[0][1]
            queue = queue[1:]
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or nx >= self.m or ny < 0 or ny >= self.n:
                    continue
                if self.visited[nx][ny] or grid[nx][ny] == "0":
                    continue
                self.visited[nx][ny] = True
                queue.append([nx, ny])
