class Solution:
    def splitArray(self, nums, m: int) -> int:
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if self.validate(nums, m, mid):
                right = mid
            else:
                left = mid + 1
        return right

    def validate(self, nums, m, size):
        number = 0
        count = 1
        for num in nums:
            if number + num <= size:
                number += num
            else:
                count += 1
                number = num
        return count <= m
