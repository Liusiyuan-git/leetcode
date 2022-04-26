class Solution:
    def subarraySum(self, nums, k: int) -> int:
        mp = {0: 1}
        pre = [0]
        ans = 0
        count = 0
        for i in range(0, len(nums)):
            count = pre[i] + nums[i]
            a = count - k
            if a in mp:
                ans += mp[a]
            if count in mp:
                mp[count] += 1
            else:
                mp[count] = 1
            pre.append(count)
        return ans
