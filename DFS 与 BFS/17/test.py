class Solution:
    def __init__(self):
        self.dic = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        self.digits = None
        self.index = 0
    def letterCombinations(self, digits: str):
        self.digits = digits
        self.index = len(digits)
        return self.dfs(0)

    def dfs(self,index):
        ans = [""]
        if index == self.index:
            return ans
        for i in self.dic[self.digits[index]]:
            for j in self.dfs(index+1):
                ans.append(i+j)
        return ans
s = Solution()
s.letterCombinations("23")