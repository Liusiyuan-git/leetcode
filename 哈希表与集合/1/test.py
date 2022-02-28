class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for index, i in enumerate(nums):
            a = target - i
            if a in dic:
                return [dic[a], index]
            dic[i] = index
