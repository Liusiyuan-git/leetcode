class Node:
    def __init__(self):
        self.l = None
        self.r = None
        self.sum = 0


class SegmentTree:

    def __init__(self, m):
        self.tree = [Node() for _ in range(4 * m + 1)]
        self.build(1, 0, m - 1)

    def build(self, p, l, r):
        self.tree[p].l = l
        self.tree[p].r = r
        if l == r:
            self.tree[p].sum = 0
            return
        mid = (l + r) // 2
        self.build(2 * p, l, mid)
        self.build(2 * p + 1, mid + 1, r)
        self.tree[p].sum = self.tree[2 * p].sum + self.tree[2 * p + 1].sum

    def add(self, p, x, val):
        l = self.tree[p].l
        r = self.tree[p].r
        if l == x == r:
            self.tree[p].sum += val
            return
        mid = (l + r) // 2
        if x <= mid:
            self.add(2 * p, x, val)
        else:
            self.add(2 * p + 1, x, val)
        self.tree[p].sum = self.tree[2 * p].sum + self.tree[2 * p + 1].sum

    def query(self, p, left, right):
        l = self.tree[p].l
        r = self.tree[p].r
        if left <= l <= r <= right:
            return self.tree[p].sum
        ans = 0
        mid = (l + r) // 2
        if left <= mid:
            ans += self.query(2 * p, left, right)
        if right > mid:
            ans += self.query(2 * p + 1, left, right)
        return ans

    def update(self, index: int, val: int) -> None:
        self.change(1, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.query(1, left, right)


class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        n = len(nums)
        sumBox = [0] * (n + 1)
        values = []
        for i in range(1, n + 1):
            sumBox[i] = sumBox[i - 1] + nums[i - 1]
        for i in range(0, n + 1):
            values.append(sumBox[i])
            values.append(sumBox[i] - upper)
            values.append(sumBox[i] - lower)
        values.sort()
        m = 0
        v = []
        for i in range(len(values)):
            if i == 0 or values[i] != values[i - 1]:
                v += [values[i]]
                m += 1
        values = v
        ans = 0
        tree = SegmentTree(m)
        tree.add(1, self.getHashValue(sumBox[0], values, m), 1)
        for i in range(1, n + 1):
            ans += tree.query(1, self.getHashValue(sumBox[i] - upper, values, m),
                              self.getHashValue(sumBox[i] - lower, values, m))
            tree.add(1, self.getHashValue(sumBox[i], values, m), 1)
        return ans

    def getHashValue(self, val, values, m):
        left = 0
        right = m - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid] == val:
                return mid
            if val < values[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
