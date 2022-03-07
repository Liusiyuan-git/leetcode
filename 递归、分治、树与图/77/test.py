class Solution:
    def __init__(self):
        self.ans = []
        self.n = 0
        self.k = 0
    def combine(self, n: int, k: int):
        self.n = n
        self.k = k
        self.recur([],1)
        return self.ans

    def recur(self, chosen, i):
        if self.n + 1 == i:
            if len(chosen) == self.k:
                self.ans.append(chosen + [])
            return

        self.recur(chosen, i + 1)
        chosen.append(i)
        self.recur(chosen, i + 1)
        chosen.pop()
