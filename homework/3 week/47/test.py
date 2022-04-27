class Solution:
    def __init__(self):
        self.vis = None

    def permuteUnique(self, nums):
        ans = []
        pre = []
        n = len(nums)
        nums.sort()
        self.vis = [False] * n
        self.back(nums, ans, 0, pre)
        return ans

    def back(self, nums, ans, index, pre):
        if index == len(nums):
            ans.append(pre[:])
            return

        for i in range(len(nums)):
            if self.vis[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not self.vis[i - 1]:
                continue
            self.vis[i] = True
            pre.append(nums[i])
            self.back(nums, ans, index + 1, pre)
            self.vis[i] = False
            pre.pop()
