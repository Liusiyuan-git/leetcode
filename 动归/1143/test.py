class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        text1 = " " + text1
        text2 = " " + text2
        f = [[0] * (n + 1)] * (m + 1)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i] == text2[j]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i][j - 1], f[i - 1][j])
        print(f)
        return f[m][n]


s = Solution()
s.longestCommonSubsequence("abcba", "abcbcba")
