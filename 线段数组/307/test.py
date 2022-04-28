class Node:
    def __init__(self):
        self.l = None
        self.r = None
        self.sum = 0


class NumArray:

    def __init__(self, nums):
        n = len(nums)
        self.tree = [Node() for _ in range(4 * n + 1)]
        self.build(nums, 1, 0, n - 1)

    def build(self, nums, p, l, r):
        self.tree[p].l = l
        self.tree[p].r = r
        if l == r:
            print(p, l)
            self.tree[p].sum = nums[l]
            return
        mid = (l + r) // 2
        self.build(nums, 2 * p, l, mid)
        self.build(nums, 2 * p + 1, mid + 1, r)
        self.tree[p].sum = self.tree[2 * p].sum + self.tree[2 * p + 1].sum

    def change(self, p, x, val):
        l = self.tree[p].l
        r = self.tree[p].r
        if l == x == r:
            self.tree[p].sum = val
            return
        mid = (l + r) // 2
        if x <= mid:
            self.change(2 * p, x, val)
        else:
            self.change(2 * p + 1, x, val)
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

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)