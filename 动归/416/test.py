class Solution:
    def canPartition(self, nums) -> bool:
        n = len(nums)
        nums = [0] + nums
        count = sum(nums)
        if count % 2 != 0:
            return False
        f = [False] * (count + 1)
        f[0] = True
        for i in range(1, n+1):
            for j in range(count, nums[i]-1, -1):
                f[j] = f[j] or f[j - nums[i]]
        return f[count//2]
