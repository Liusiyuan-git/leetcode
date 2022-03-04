class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                for j in self.twoSum(nums, i + 1, -1 * nums[i]):
                    ans.append([nums[i], j[0], j[1]])
        return ans

    def twoSum(self, numbers, start, target):
        ans = []
        j = len(numbers) - 1
        for i in range(start, len(numbers)):
            if i > start and numbers[i] == numbers[i - 1]:
                continue
            while i < j and numbers[i] + numbers[j] > target:
                j -= 1
            if i < j and numbers[i] + numbers[j] == target:
                ans.append([numbers[i], numbers[j]])
        return ans