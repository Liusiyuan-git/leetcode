class Solution:
    def maxProfit(self, prices) -> int:
        ans = 0
        for i in range(len(prices)):
            if i > 0:
                ans += max(prices[i] - prices[i - 1], 0)
        return ans