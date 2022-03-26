from functools import cmp_to_key


class Solution:
    def __init__(self):
        self.arr2 = None
        self.arr2orders = None

    def relativeSortArray(self, arr1, arr2):
        self.arr2 = arr2
        self.arr2orders = {}
        for i in range(len(arr2)):
            self.arr2orders[arr2[i]] = i
        arr1 = sorted(arr1, key=cmp_to_key(self.sort))
        return arr1

    def sort(self, x, y):
        if x in self.arr2orders:
            xPos = self.arr2orders[x]
        else:
            xPos = len(self.arr2)
        if y in self.arr2orders:
            yPos = self.arr2orders[y]
        else:
            yPos = len(self.arr2)
        if xPos > yPos:
            return 1
        elif xPos < yPos:
            return -1
        if xPos == yPos:
            if x > y:
                return 1
            else:
                return -1
