class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        f = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    f[i] = max(f[i], f[j] + 1)
        return max(f)
