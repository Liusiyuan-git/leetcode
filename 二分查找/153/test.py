class Solution:
    def findMin(self, nums) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid + 1
        return nums[right]