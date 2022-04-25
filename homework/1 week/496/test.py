class Solution:
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums1)
        ans = [-1] * n
        hashMap = {}
        stack = []
        for i in nums2:
            while stack and stack[-1] < i:
                hashMap[stack[-1]] = i
                stack.pop()
            stack.append(i)

        for i in range(n):
            if nums1[i] in hashMap:
                ans[i] = hashMap[nums1[i]]
        return ans