class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        word1 = " " + word1
        word2 = " " + word2
        f = [[1e9 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            f[i][0] = i
        for j in range(m+1):
            f[0][j] = j
        for i in range(1, n+1):
            for j in range(1,m+1):
                f[i][j] = min(f[i][j-1]+1, f[i-1][j]+1, f[i-1][j-1]+(word1[i] != word2[j]))
        return f[n][m]