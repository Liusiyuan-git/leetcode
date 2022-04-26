class Solution:
    def findShortestSubArray(self, nums) -> int:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = [1, i, i]
            else:
                hashMap[nums[i]][0] += 1
                hashMap[nums[i]][2] = i
        maxNum = 0
        minLen = int(1e9)
        for i in hashMap.keys():
            arr = hashMap[i]
            if arr[0]> maxNum:
                maxNum = arr[0]
                minLen = arr[2] - arr[1] + 1
            elif arr[0] ==  maxNum:
                minLen = min(minLen, arr[2] - arr[1] + 1)
        return minLen