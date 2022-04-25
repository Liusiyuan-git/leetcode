class Solution:
    def nextGreaterElements(self, nums):
        l = len(nums)
        n = 2 * l
        ans = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1] % l] < nums[i % l]:
                ans[stack[-1]] = nums[i % l]
                stack.pop()
            stack.append(i)
        return ans[:l]