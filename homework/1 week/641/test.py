class MyCircularDeque:

    def __init__(self, k: int):
        self.dequeue = []
        self.count = k


    def insertFront(self, value: int) -> bool:
        if self.count > 0:
            self.dequeue = [value] + self.dequeue
            self.count -= 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.count > 0:
            self.dequeue += [value]
            self.count -= 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.dequeue:
            return False
        self.dequeue = self.dequeue[1:]
        self.count += 1
        return True

    def deleteLast(self) -> bool:
        if not self.dequeue:
            return False
        self.dequeue.pop()
        self.count += 1
        return True

    def getFront(self) -> int:
        if self.dequeue:
            return self.dequeue[0]
        return -1

    def getRear(self) -> int:
        if self.dequeue:
            return self.dequeue[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.dequeue) == 0

    def isFull(self) -> bool:
        return self.count == 0


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()