class MinStack:

    def __init__(self):
        self.stack = []
        self.miniArr = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.miniArr:
            self.miniArr.append(val)
        else:
            min_v = self.miniArr[-1]
            if min_v <= val:
                self.miniArr.append(min_v)
            else:
                self.miniArr.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.miniArr.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.miniArr[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
