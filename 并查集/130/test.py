class Solution:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.fa = None

    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.n = len(board)
        self.m = len(board[0])
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        outside = self.n * self.m
        self.fa = [0] * (self.n * self.m + 1)
        for i in range(0, self.n * self.m + 1):
            self.fa[i] = i

        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == "X":
                    continue
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if ni < 0 or ni >= self.n or nj < 0 or nj >= self.m:
                        self.UnionSet(self.num(i, j), outside)
                    else:
                        if board[ni][nj] == "O":
                            self.UnionSet(self.num(i, j), self.num(ni, nj))
        outside = self.find(outside)
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == "O" and self.find(self.num(i, j)) != outside:
                    board[i][j] = "X"

    def num(self, i, j):
        return i * self.m + j

    def find(self, x):
        if x == self.fa[x]:
            return x
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def UnionSet(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.fa[x] = y
