class Solution:
    def __init__(self):
        self.depth = {}
        self.q = []

    def slidingPuzzle(self, board) -> int:
        start = self.zip(board)
        target = "123450"
        self.q.append(start)
        self.depth[start] = 0
        while self.q:
            s = self.q[0]
            self.q = self.q[1:]
            pos = self.findZeroIndex(s)
            if pos >= 3:
                self.expend(s, pos, pos - 3)
            if pos <= 2:
                self.expend(s, pos, pos + 3)
            if pos % 3 != 0:
                self.expend(s, pos, pos - 1)
            if pos % 3 != 2:
                self.expend(s, pos, pos + 1)
            if target in self.depth:
                return self.depth[target]
        return -1

    def expend(self, s, i, j):
        ns = list(s)
        ns[i], ns[j] = ns[j], ns[i]
        ns = "".join(ns)
        if ns in self.depth:
            return
        self.depth[ns] = self.depth[s] + 1
        self.q.append(ns)

    def zip(self, board):
        s = ""
        for i in board:
            for j in i:
                s += str(j)
        return s

    def findZeroIndex(self, s):
        for i in range(6):
            if s[i] == "0":
                return i
