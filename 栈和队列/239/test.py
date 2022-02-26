class Solution:
    def maxSlidingWindow(self, nums, k: int):
        dequeue = []
        ans = []
        for i in range(0, len(nums)):
            if dequeue and i - k >= dequeue[0]:
                dequeue = dequeue[1:]
            while dequeue and nums[dequeue[-1]] < nums[i]:
                dequeue.pop()
            dequeue.append(i)
            if i + 1 - k >= 0:
                ans.append(nums[dequeue[0]])
        return ans
