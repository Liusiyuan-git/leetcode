class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        left = 0
        right = n * m - 1
        while left <= right:
            mid = (left + right) // 2
            nx = mid // m
            ny = mid % m
            if matrix[nx][ny] > target:
                right = mid - 1
            elif matrix[nx][ny] < target:
                left = mid + 1
            else:
                return True
        return False