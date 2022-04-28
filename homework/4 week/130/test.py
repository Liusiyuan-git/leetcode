class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.n = len(board)
        self.m = len(board[0])
        for i in range(self.n):
            self.dfs(board, i, 0)
            self.dfs(board, i, self.m - 1)

        for j in range(self.m):
            self.dfs(board, 0, j)
            self.dfs(board, self.n - 1, j)

        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "A":
                    board[i][j] = "O"

    def dfs(self, board, x, y):
        if x < 0 or x == self.n or y < 0 or y == self.m or board[x][y] != "O":
            return
        board[x][y] = "A"
        self.dfs(board, x + 1, y)
        self.dfs(board, x - 1, y)
        self.dfs(board, x, y + 1)
        self.dfs(board, x, y - 1)
