class Solution:
    def __init__(self):
        self.nums1 = None
        self.f = None

    def maxCoins(self, nums) -> int:
        n = len(nums)
        self.nums1 = [1] + nums + [1]
        self.f = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                self.f[i][j] = -1

        return self.calc(1, n)

    def calc(self, l, r):
        if l > r:
            return 0
        if self.f[l][r] != -1:
            return self.f[l][r]
        for p in range(l, r + 1):
            self.f[l][r] = max(self.f[l][r],
                               self.calc(l, p - 1) + self.calc(p + 1, r) + self.nums1[p] * self.nums1[l - 1] *
                               self.nums1[r + 1])
        return self.f[l][r]



