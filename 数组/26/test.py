class Solution:
    def removeDuplicates(self, nums):
        count = 0
        for index, i in enumerate(nums):
            if index == 0 or nums[index] != nums[index - 1]:
                nums[count] = i
                count += 1

        return count

s = Solution()
s.removeDuplicates([1, 2, 3, 4, 4, 4, 6, 6, 7])
