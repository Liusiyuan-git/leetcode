class Solution:
    def topKFrequent(self, nums, k: int):
        p = {}
        for i in nums:
            if i not in p:
                p[i] = 1
            else:
                p[i] += 1

        p = sorted(list(p.items()), key=lambda x: x[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(p[i][0])
        return ans
