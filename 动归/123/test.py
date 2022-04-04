class Solution:
    def maxProfit(self, prices) -> int:
        k = 2
        prices = [0] + prices
        n = len(prices)
        f = [[[-1e9 for _ in range(k + 1)] for _ in range(2)] for _ in range(n)]
        f[0][0][0] = 0
        for i in range(1, n):
            for j in range(2):
                for c in range(k + 1):
                    if c > 0:
                        f[i][1][c] = max(f[i][1][c], f[i - 1][0][c - 1] - prices[i])
                    f[i][0][c] = max(f[i][0][c], f[i - 1][1][c] + prices[i])
                    f[i][j][c] = max(f[i][j][c], f[i - 1][j][c])
        ans = 0
        for i in range(0, k + 1):
            ans = max(ans, f[n - 1][0][i])
        return ans
