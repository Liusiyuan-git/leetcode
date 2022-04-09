class Solution:
    def mergeStones(self, stones, k: int) -> int:
        n = len(stones)
        f = [[[1e9 for _ in range(k + 1)]for _ in range(n)] for _ in range(n)]
        for l in range(0, n):
            f[l][l][1] = 0
        for length in range(2, n+1):
            for l in range(0, n - length + 1):
                r = l + length -1
                for i in range(2, k+1):
                    for p in range(l, r):
                        f[l][r][i] = min(f[l][r][i], f[l][p][1] + f[p+1][r][i-1])
                sum1 = 0
                for p in range(l, r+1):
                    sum1 += stones[p]
                f[l][r][1] = min(f[l][r][1], f[l][r][k] + sum1)
        if f[0][n-1][1] == 1e9:
            return -1
        else:
            return f[0][n-1][1]