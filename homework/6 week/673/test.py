class Solution:
    def findNumberOfLIS(self, nums) -> int:
        n = len(nums)
        maxLen = maxSize = 0
        f = [1] * n
        cnt = [1] * n
        for i in range(n):
            f[i] = 1
            cnt[i] = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if f[j] + 1 > f[i]:
                        f[i] = f[j] + 1
                        cnt[i] = cnt[j]
                    elif f[j] + 1 == f[i]:
                        cnt[i] += cnt[j]
            if f[i] > maxLen:
                maxLen = f[i]
                maxSize = cnt[i]
            elif f[i] == maxLen:
                maxSize += cnt[i]
        return maxSize
