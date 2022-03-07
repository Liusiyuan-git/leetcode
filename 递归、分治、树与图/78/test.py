class Solution:
    def __init__(self):
        self.ans = []
        self.size = 0

    def subsets(self, nums):
        self.size = len(nums)
        self.recur([], nums, 0)
        return self.ans

    def recur(self, chosen, nums, i):
        if self.size == i:
            self.ans.append(chosen + [])
            return

        self.recur(chosen, nums, i + 1)
        chosen.append(nums[i])
        self.recur(chosen, nums, i + 1)
        chosen.pop()

