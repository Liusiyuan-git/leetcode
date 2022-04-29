class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        s = 0
        sumValue = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            s += nums[i]
            sumValue[i+1] = s
        return self.caculate(sumValue, lower, upper, 0, len(sumValue) - 1)

    def caculate(self, sumValue, lower, upper, left, right):
        if left == right:
            return 0
        mid = (left + right) // 2
        n1 = self.caculate(sumValue, lower, upper, left, mid)
        n2 = self.caculate(sumValue, lower, upper, mid+1, right)
        ret = n1 + n2

        i = left
        l = mid +1
        r = mid+1
        while i <= mid:
            while l <= right and sumValue[l] - sumValue[i] < lower:
                l += 1
            while r <= right and sumValue[r] - sumValue[i] <= upper:
                r += 1
            ret += r - l
            i += 1

        sortedArr = []
        for i in range(left, right+1):
            sortedArr.append(sumValue[i])
        sortedArr.sort()
        for j in range(len(sortedArr)):
            sumValue[left+j] = sortedArr[j]
        return ret
