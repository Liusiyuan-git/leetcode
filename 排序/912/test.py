import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        self.quickSort(nums, left, right)
        return nums

    def quickSort(self, arr, l, r):
        if l >= r:
            return
        privot = self.partition(arr, l, r)
        self.quickSort(arr, l, privot)
        self.quickSort(arr, privot + 1, r)

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