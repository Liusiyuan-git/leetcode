class Solution:
    def __init__(self):
        self.n = None
        self.p = []
        self.used = []
        self.ans = []
        self.usedPlus = {}
        self.usedMinus = {}
    def solveNQueens(self, n: int):
        self.n = n
        self.used = [False] * n
        self.dfs(0)
        result = []
        for i in self.ans:
            result.append([])
            for j in i:
                a = ["."] * n
                a[j] = "Q"
                result[-1].append("".join(a))
        return result


    def dfs(self,row):
        if row == self.n:
            self.ans.append(self.p + [])
            return
        for col in range(0,self.n):
            sum = row + col
            sub = row - col
            if not self.used[col] and (sum not in self.usedPlus or not self.usedPlus[sum]) and (sub not in self.usedMinus or not self.usedMinus[sub]):
                self.p.append(col)
                self.used[col] = True
                self.usedPlus[sum] = True
                self.usedMinus[sub] = True
                self.dfs(row+1)
                self.usedPlus[sum] = False
                self.usedMinus[sub] = False
                self.used[col] = False
                self.p.pop()
