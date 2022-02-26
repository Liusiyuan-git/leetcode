class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = {
            "queue": [],
            "length": k
        }

    def insertFront(self, value: int) -> bool:
        if self.queue["length"] == 0:
            return False
        else:
            self.queue["queue"] = [value] + self.queue["queue"]
            self.queue["length"] -= 1
            return True

    def insertLast(self, value: int) -> bool:
        if self.queue["length"] == 0:
            return False
        else:
            self.queue["queue"].append(value)
            self.queue["length"] -= 1
            return True

    def deleteFront(self) -> bool:
        if not self.queue["queue"]:
            return False
        else:
            self.queue["queue"] = self.queue["queue"][1:]
            self.queue["length"] += 1
            return True

    def deleteLast(self) -> bool:
        if not self.queue["queue"]:
            return False
        else:
            self.queue["queue"].pop()
            self.queue["length"] += 1
            return True

    def getFront(self) -> int:
        if not self.queue["queue"]:
            return -1
        else:
            return self.queue["queue"][0]

    def getRear(self) -> int:
        if not self.queue["queue"]:
            return -1
        else:
            return self.queue["queue"][-1]

    def isEmpty(self) -> bool:
        if not self.queue["queue"]:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.queue["length"] == 0:
            return True
        else:
            return False

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
