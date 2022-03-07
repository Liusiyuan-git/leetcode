class Solution:
    def __init__(self):
        self.ans = []
        self.used = []
        self.n = 0

    def permute(self, nums) :
        self.n = len(nums)
        self.used = [False] * self.n
        self.recur([], 0, nums)
        return self.ans

    def recur(self, container, num, nums):
        if num == self.n:
            self.ans.append(container + [])
            return
        for i in range(0, len(nums)):
            if not self.used[i]:
                container.append(nums[i])
                self.used[i] = True
                self.recur(container, num + 1, nums)
                self.used[i] = False
                container.pop()
