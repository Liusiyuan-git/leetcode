class Solution:
    def __init__(self):
        self.hashBank = {}
        self.depth = {}

    def minMutation(self, start: str, end: str, bank) -> int:
        for i in bank:
            self.hashBank[i] = 1
        self.depth[start] = 0
        queue = [start]
        g = ["A", "C", "G", "T"]
        while queue:
            s = queue[0]
            queue = queue[1:]
            for i in range(8):
                for j in g:
                    ns = list(s)
                    if ns[i] == j:
                        continue
                    ns[i] = j
                    ns = "".join(ns)
                    if ns not in self.hashBank:
                        continue
                    if ns in self.depth:
                        continue
                    self.depth[ns] = self.depth[s] + 1
                    if ns == end:
                        return self.depth[ns]
                    queue.append(ns)
        return -1
