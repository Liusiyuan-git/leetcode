import random


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        return self.quickSort(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSort(self, arr, l, r, index):
        if l >= r:
            return arr[l]
        privot = self.partition(arr, l, r)
        if index <= privot:
            return self.quickSort(arr, l, privot, index)
        else:
            return self.quickSort(arr, privot + 1, r, index)

    def partition(self, a, l, r):
        pivot = l + int(random.random() * (r - l + 1))
        pivotVal = a[pivot]
        while l <= r:
            while a[l] < pivotVal:
                l += 1
            while a[r] > pivotVal:
                r -= 1
            if l == r:
                break
            if l < r:
                a[l], a[r] = a[r], a[l]
                l += 1
                r -= 1
        return r
