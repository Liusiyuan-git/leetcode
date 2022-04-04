class Solution:
    def maxProfit(self, prices) -> int:
        prices = [0] + prices
        n = len(prices)
        f = [[-1e9 for _ in range(2)] for _ in range(n)]
        f[0][0] = 0
        for i in range(1, n):
            f[i][1] = max(f[i][1], f[i - 1][0] - prices[i])
            f[i][0] = max(f[i][0], f[i - 1][1] + prices[i])
            for j in range(2):
                f[i][j] = max(f[i][j], f[i - 1][j])
        return f[n - 1][0]
