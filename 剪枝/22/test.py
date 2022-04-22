class Solution:
    def __init__(self):
        self.n = 0
        self.ans = []
        self.s = []

    def generateParenthesis(self, n: int):
        self.n = n
        self.dfs(0, 0, 0)
        return self.ans

    def dfs(self, i, l, r):
        if l > self.n or r > self.n or not self.IsValidate(self.s):
            return
        if i == 2 * self.n:
            self.ans.append("".join(self.s))
        self.s.append("(")
        self.dfs(i + 1, l + 1, r)
        self.s.pop()
        self.s.append(")")
        self.dfs(i + 1, l, r + 1)
        self.s.pop()

    def IsValidate(self, arr):
        left = 0
        for i in arr:
            if i == "(":
                left += 1
            else:
                if left <= 0:
                    return False
                left -= 1
        return True
