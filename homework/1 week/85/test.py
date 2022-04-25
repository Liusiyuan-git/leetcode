class Solution:
    def maximalRectangle(self, matrix) -> int:
        m = len(matrix)
        n = len(matrix[0])
        left = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if j == 0:
                        left[i][j] = 1
                    else:
                        left[i][j] = left[i][j - 1] + 1

        ans = 0
        for j in range(n):
            stack = []
            up = [0] * m
            down = [0] * m
            for i in range(m):
                while stack and left[stack[-1]][j] >= left[i][j]:
                    stack.pop()
                if stack:
                    up[i] = stack[-1]
                else:
                    up[i] = -1
                stack.append(i)
            stack = []
            for i in range(m - 1, -1, -1):
                while stack and left[stack[-1]][j] >= left[i][j]:
                    stack.pop()
                if stack:
                    down[i] = stack[-1]
                else:
                    down[i] = m
                stack.append(i)

            for i in range(m):
                height = down[i] - up[i] - 1
                area = left[i][j] * height
                ans = max(ans, area)
        return ans
