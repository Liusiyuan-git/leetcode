class Solution:
    def coinChange(self, coins, amount: int) -> int:
        opt = [0] * (amount + 1)
        INF = int(1e9)
        opt[0] = 0
        for i in range(1,amount + 1):
            opt[i] = INF
            for j in range(0, len(coins)):
                if i - coins[j] >= 0:
                    opt[i] = min(opt[i],opt[i - coins[j]]+1)
        if opt[amount] >= INF:
            opt[amount] = -1
        return opt[amount]