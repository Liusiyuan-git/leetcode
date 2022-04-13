class Solution:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.fa = []  # 定义并查集fa数组

    def numIslands(self, grid) -> int:
        self.n = len(grid)  # 数组行数
        self.m = len(grid[0])  # 数组列数
        dx = [0, 1]  # 定义方向数组
        dy = [1, 0]
        outside = self.n * self.m  # 域外点，凡事0都跟它一个子集
        ans = set()  # 开一个结果集合存结果
        for i in range(self.n * self.m + 1):
            self.fa.append(i)  # 初始化fa数组
        for i in range(self.n):  # 开始探索
            for j in range(self.m):
                if grid[i][j] == "0":  # 如果是0点，就跟域外点一个子集
                    self.UnionSet(self.num(i, j), outside)
                    continue
                for k in range(2):  # 如果是1点，由方向数组，往右，往下走就可以，因为往左和往上随着外层for遍历一定会走到
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if ni < 0 or ni == self.n or nj < 0 or nj == self.m:  # 判断是否越界
                        continue
                    else:
                        if grid[ni][nj] == "1":  # 不越界且为1点，表明相连，加入并查集
                            self.UnionSet(self.num(i, j), self.num(ni, nj))

        for i in range(self.n * self.m):
            if self.fa[i] != outside:  # 不等于域外点，说明不是0点，加入结果集合
                ans.add(self.find(self.fa[i]))
        return len(ans)  # 返回长度就是岛屿数量

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
