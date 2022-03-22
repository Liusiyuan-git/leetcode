class Solution:
    def findPeakElement(self, nums) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            lmid = (left + right) // 2
            rmid = lmid + 1
            if nums[lmid] <= nums[rmid]:
                left = lmid + 1
            else:
                right = rmid - 1
        return right
