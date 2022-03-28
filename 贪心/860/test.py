class Solution:
    def __init__(self):
        self.dic = {}

    def lemonadeChange(self, bills) -> bool:
        self.dic[5] = 0
        self.dic[10] = 0
        self.dic[20] = 0
        for i in bills:
            self.dic[i] += 1
            if not self.exchange(i - 5):
                return False
        return True

    def exchange(self, val):
        for i in [20, 10, 5]:
            while self.dic[i] > 0 and val >= i:
                self.dic[i] -= 1
                val -= i
        return val == 0
