import heapq
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        queue = []
        ans = []
        for i in range(0,len(nums)):
            if i - k + 1 < 0:
                heapq.heappush(queue,(-1 * nums[i],i))
            elif i - k + 1 == 0:
                heapq.heappush(queue, (-1 * nums[i], i))
                ans.append(nums[queue[0][1]])
            else:
                print(queue, i, k)
                while i - k >= queue[0][1]:
                    heapq.heappop(queue)
                heapq.heappush(queue,(-1 * nums[i],i))
                ans.append(nums[queue[0][1]])
        return ans

s = Solution()
s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 1)
