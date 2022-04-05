class Solution:
    def rob(self, nums) -> float:
        n = len(nums)
        f = [[-1e9 for _ in range(2)] for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            f[i][0] = max(f[i - 1][0], f[i - 1][1])
            f[i][1] = f[i - 1][0] + nums[i - 1]
        return max(f[n][0], f[n][1])
