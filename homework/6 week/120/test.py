class Solution:
    def minimumTotal(self, triangle) -> int:
        n = len(triangle)
        m = len(triangle[n - 1])
        f = [[0 for _ in range(m)] for _ in range(n)]
        f[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(m):
                if j == 0:
                    f[i][0] = f[i - 1][0] + triangle[i][0]
                    continue
                if i == j:
                    f[i][j] = f[i - 1][j - 1] + triangle[i][j]
                    break

                f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
        ans = int(1e9)
        for i in range(m):
            ans = min(ans, f[n - 1][i])
        return ans