class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        n = len(nums)
        nums = [0] + nums
        ss = [0] * (2*n + 1)
        for i in range(1,n+1):
            ss[i] = ss[i-1] + nums[i]
        for i in range(n+1, 2*n+1):
            ss[i] = ss[i-1] + nums[i-n]
        q = []
        ans = -1e9
        for i in range(1, 2*n + 1):
            while q and q[0] < i - n:
                q = q[1:]
            if q:
                ans = max(ans, ss[i] - ss[q[0]])
            while q and ss[q[-1]] >= ss[i]:
                    q.pop()
            q.append(i)
        return ans
