class Solution:
    def maxProfit(self, prices) -> int:
        prices = [0] + prices
        n = len(prices)
        f = [[[-1e9 for _ in range(2)] for _ in range(2)] for _ in range(n)]
        f[0][0][0] = 0
        for i in range(1, n):
            for j in range(2):
                for l in range(2):
                    f[i][1][0] = max(f[i][1][0], f[i - 1][0][0] - prices[i])
                    f[i][0][1] = max(f[i][0][1], f[i - 1][1][0] + prices[i])
                    f[i][j][0] = max(f[i][j][0], f[i - 1][j][l])
        return max(f[n - 1][0][0], f[n - 1][0][1])
