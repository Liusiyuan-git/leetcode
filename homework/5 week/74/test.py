class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        arr = []
        for i in matrix:  # 二维变一维
            arr += i
        left = -1
        right = len(arr) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if arr[mid] <= target:
                left = mid
            else:
                right = mid - 1
        if right < 0 or right >= len(arr) or arr[right] != target: # 讨论不存在的情况：太小，比矩阵最小的还小；太大，比矩阵最大的还大；夹中间
            return False
        else:
            return True
