class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        tmp = []
        count = 0
        ans = 0
        map = {0: 1}
        for i in nums:
            tmp.append(i % 2)
        for j in tmp:
            count += j
            s = count - k
            if s in map:
                ans += map[s]
            if count not in map:
                map[count] = 1
            else:
                map[count] += 1
        return ans

