class Solution:
    def __init__(self):
        self.n = 0  # 全局定义宽度
        self.m = 0  # 全局定义高度
        self.visited = {}  # 记录哪些点被访问过了
        self.board = None  # 定义全局board
        self.p = True  # 记录区域是否有边界点
        self.ans = []  # 记录可以被置成"X"的坐标

    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.n = len(board)  # 宽度初始化
        self.m = len(board[0])  # 高度初始化
        self.board = board  # 全局board
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == "O" and self.num(i, j) not in self.visited:  # 如果是"O", 并且没有被访问过，则可以进行访问
                    self.p = True  # 每次都要重置
                    self.dfs(i, j)  # 开始 dfs探索
                    if self.p:  # 区域合法，没有边界点，则可以置成 "X"
                        for ans in self.ans:
                            board[ans[0]][ans[1]] = "X"
                    self.ans = []  # 重置 ans

    def dfs(self, x, y):
        self.visited[self.num(x, y)] = 1  # 进来了就表明该点访问过了
        nx = [-1, 0, 0, 1]  # 方向数组，上下移动
        ny = [0, -1, 1, 0]  # 方向数组，左右移动
        for i in range(4):  # 开始探索四周的点
            xx = x + nx[i]
            yy = y + ny[i]
            if xx < 0 or xx == self.n or yy < 0 or yy == self.m:  # 边界点，非法
                self.p = False
                continue
            if self.board[xx][yy] == "O" and self.num(xx, yy) not in self.visited:  # 合法点
                self.dfs(xx, yy)
        self.ans.append([x, y])  # 将访问过的点，放置于 ans, 便于后续处理

    def num(self, x, y):
        return x * self.m + y
