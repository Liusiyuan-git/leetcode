class Solution:
    def findMin(self, nums) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:  # left == right 的时候退出
            mid = (left + right) // 2
            if nums[mid] < nums[right]:  # 比右边小，右边压缩
                right = mid
            elif nums[mid] > nums[right]:  # 比右边大，左边前进
                left = mid + 1
            else:  # 相等，右边压缩
                right -= 1
        return nums[right]
