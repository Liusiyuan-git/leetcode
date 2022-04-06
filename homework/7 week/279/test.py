class Solution:
    def numSquares(self, n: int) -> int:
        s = []  # 定义完全平方数数组s
        for i in range(1, n + 1):  # 算出，在n范围内，有多少数属于完全平方数，存到s里
            if i ** 2 <= n:
                s.append(i ** 2)
        l = len(s)  # s的长度 l
        s = [0] + s  # 从下标1开始算
        f = [1e9] * (n + 1)  # f[i,j]是，从前i种完全平方数中，选出了总和为j的数，数量的最小值
        f[0] = 0  # 没选，值是0
        for i in range(1, l + 1):  # 套用完全背包模版
            for j in range(s[i], n + 1):
                f[j] = min(f[j], f[j - s[i]] + 1)
        return f[n]  # 返回最终值
