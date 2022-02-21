# 法一
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        location = 0
        for i in nums:
            if i != 0:
                nums[location] = i
                location += 1
        while location < len(nums):
            nums[location] = 0
            location += 1

s = Solution()
s.moveZeroes([1, 0, 1])
