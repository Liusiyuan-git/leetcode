class Solution:
    def __init__(self):
        self.fa = []

    def minCostConnectPoints(self, points) -> int:
        n = len(points)
        edge = []
        for i in range(n):
            for j in range(i + 1, n):
                edge.append([i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])])

        edge = sorted(edge, key=lambda x: x[2])
        for i in range(n):
            self.fa.append(i)
        ans = 0
        for i in edge:
            if self.find(i[0]) != self.find(i[1]):
                ans += i[2]
                self.UnionSet(i[0], i[1])
        return ans

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
