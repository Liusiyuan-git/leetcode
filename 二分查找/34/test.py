class Solution:
    def searchRange(self, nums, target: int):
        ans = []
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        ans.append(right)

        left = -1
        right = len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        ans.append(right)
        if ans[0] > ans[1]:
            return [-1, -1]
        return ans


