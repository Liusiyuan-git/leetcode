class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.a = [0] * (self.n+1)
        self.c = [0] * (self.n+1)
        for i in range(1, self.n+1):
            self.a[i] = nums[i-1]
            self.add(i, self.a[i])


    def update(self, index: int, val: int) -> None:
        index += 1
        self.add(index, val - self.a[index])
        self.a[index] = val

    def sumRange(self, left: int, right: int) -> int:
        left += 1
        right += 1
        return self.query(right) - self.query(left - 1)

    def add(self, x, delta):
        while x <= self.n:
            self.c[x] += delta
            x += self.lowbit(x)

    def query(self, x):
        ans = 0
        while x > 0:
            ans += self.c[x]
            x -= self.lowbit(x)
        return ans

    def lowbit(self, x):
        return x & -x



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)