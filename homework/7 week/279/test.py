class Solution:
    def numSquares(self, n: int) -> int:
        f = [0] * (n+1)
        for i in range(1, n+1):
            minv = int(1e9)
            j = 1
            while j * j <= i:
                minv = min(minv, f[i - j * j])
                j += 1
            f[i] = minv + 1
        return f[n]