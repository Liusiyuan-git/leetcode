class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        s = " " + s
        p = " " + p
        f = [[False for _ in range(m + 1)] for _ in range(n + 1)]  # 定义f[i][j]数组，表示s的前i个字符，p的前j个字符，能否匹配
        f[0][0] = True  # f初始化，空串一定匹配空串
        for j in range(1, m + 1):
            if p[j] == "*":  # '*' 可以匹配任意字符串，所以为True
                f[0][j] = True
            else:
                break

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j] >= "a" and p[j] <= "z":  # 当 p[j] 是数字，匹配的前提是 i与j的前一个 i-1 与 j-1 属否匹配，以及 i，j是否相等
                    f[i][j] = f[i - 1][j - 1] and s[i] == p[j]
                elif p[j] == "?":  # 当 p[j] 是 . ，它与任何字母都匹配，顾匹配的关键是，i与j的前一个 i-1 与 j-1 属否匹配
                    f[i][j] = f[i - 1][j - 1]
                else:  # 当 p[j] 是 #, 它与任何字串匹配，顾两个分支，跟 # 匹配，与不跟 # 匹配，两者取一
                    f[i][j] = f[i][j - 1] or f[i - 1][j]
        return f[n][m]
