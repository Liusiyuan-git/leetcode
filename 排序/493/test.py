class Solution:
    def __init__(self):
        self.ans = 0

    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(nums, 0, len(nums) - 1)
        return self.ans

    def mergeSort(self, arr, l, r):
        if l >= r:
            return
        mid = (l + r) // 2
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid + 1, r)
        self.calculate(arr, l, mid, r)
        self.merge(arr, l, mid, r)

    def calculate(self, arr, left, mid, right):
        j = mid
        for i in range(left, mid + 1):
            while j < right and arr[i] > 2 * arr[j + 1]:
                j += 1
            self.ans += j - mid

    def merge(self, arr, left, mid, right):
        temp = [0] * (right - left + 1)
        i = left
        j = mid + 1
        for k in range(0, len(temp)):
            if j > right or i <= mid and arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
        for k in range(0, len(temp)):
            arr[left + k] = temp[k]

