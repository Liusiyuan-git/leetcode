class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            result = self.search(matrix[i], 0, m-1, target)
            if result:
                return True
        return False

    def search(self, row, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if row[mid] > target:
                right = mid - 1
            elif row[mid] < target:
                left = mid + 1
            else:
                return True
        return False