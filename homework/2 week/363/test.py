class Solution:
    def maxSumSubmatrix(self, matrix, k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        ans = -int(1e9)
        for i in range(n):
            b = [0] * m
            for j in range(i, n):
                for c in range(m):
                    b[c] += matrix[j][c]
                arr = []
                arr.append(0)
                s = 0
                for v in b:
                    s += v
                    ceil = self.ceiling(arr, s - k)
                    if ceil != None:
                        ans = max(ans, s - ceil)
                    arr.append(s)
        return ans

    def ceiling(self, arr, target):
        for i in sorted(arr):
            if target <= i:
                return i
        return None
