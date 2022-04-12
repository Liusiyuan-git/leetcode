class Solution:
    def __init__(self):
        self.fa = []
    def findCircleNum(self, isConnected) -> int:
        n = len(isConnected)
        for i in range(0, n):
            self.fa.append(i)
        for i in range(0, n):
            for j in range(0, n):
                if isConnected[i][j]:
                    self.UnionSet(i, j)
        ans = 0
        for i in range(0, n):
            if i == self.Find(i):
                ans += 1
        return ans

    def Find(self, x):
        if x == self.fa[x]:
            return x
        self.fa[x] = self.Find(self.fa[x])
        return self.fa[x]

    def UnionSet(self, x, y):
        x = self.Find(x)
        y = self.Find(y)
        if x != y:
            self.fa[x] = y


