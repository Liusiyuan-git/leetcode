class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        s = " " + s
        t = " " + t
        f = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            f[i][0] = 1

        for i in range(n + 1):
            for j in range(m + 1):
                f[i][j] = f[i - 1][j]
                if s[i] == t[j]:
                    f[i][j] += f[i - 1][j - 1]
        return f[n][m]