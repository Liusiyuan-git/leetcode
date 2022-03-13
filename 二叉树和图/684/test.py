class Solution:
    def __init__(self):
        self.visited = None
        self.to = None
        self.hascycle = False
    def findRedundantConnection(self, edges):
        n = 0
        for i in edges:
            for j in i:
                n = max(n,j)
        self.to = [[] for i in range(n+1)]
        self.visited = [False] * (n+1)
        for edge in edges:
            x = edge[0]
            y = edge[1]
            self.to[x].append(y)
            self.to[y].append(x)
            self.hascycle = False
            for i in range(1, n+1):
                self.visited[i]  =False
            self.dfs(x, 0)
            if self.hascycle:
                return edge
        return []


    def dfs(self, i, fa):
        self.visited[i] = True
        for k in self.to[i]:
            if k == fa:
                continue
            if not self.visited[k]:
                self.dfs(k, i)
            else:
                self.hascycle = True
