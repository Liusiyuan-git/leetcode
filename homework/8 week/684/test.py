class Solution:
    def __init__(self):
        self.fa = None  # 定义并查集fa数组

    def findRedundantConnection(self, edges):
        n = len(edges)
        self.fa = []
        for i in range(n + 1):
            self.fa.append(i)  # 初始化fa数组
        ans = []  # 答案数组，存放答案
        for i in edges:
            if self.find(i[0]) != self.find(i[1]):  # 查询两个点是否在并查集里，不在并查集里，则说明它们没有连在一起，那就加入并查集
                self.UnionSet(i[0], i[1])
            else:
                ans.append(i)  # 如果都在并查集里，说明它们之前就已经连起来了，这条边再加一条边就构成环，所有这条边是答案之一
        return ans[-1]  # 由于时间顺序，数组的最后一条边一定就是答案

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
