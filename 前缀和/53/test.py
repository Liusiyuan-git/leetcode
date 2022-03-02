class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        s = [0] * (n + 1)
        preMin = [0] * (n + 1)
        for i in range(1, n + 1):
            s[i] = s[i - 1] + nums[i - 1]
        for i in range(1, n + 1):
            preMin[i] = min(s[i], preMin[i - 1])
        ans = -100000
        for i in range(1, n + 1):
            ans = max(ans, s[i] - preMin[i - 1])
        return ans
