class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        s = " " + s
        p = " " + p
        f = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        f[0][0] = True
        for j in range(2, m + 1, 2):
            if p[j] == "*":
                f[0][j] = True
            else:
                break
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j] >= "a" and p[j] <= "z":
                    f[i][j] = f[i - 1][j - 1] and s[i] == p[j]
                elif p[j] == ".":
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = f[i][j - 2]
                    if s[i] == p[j - 1] or p[j - 1] == ".":
                        f[i][j] = f[i][j] or f[i - 1][j]
        return f[n][m]
