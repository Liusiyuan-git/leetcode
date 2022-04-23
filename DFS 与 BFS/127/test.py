class Solution:
    def __init__(self):
        self.wordSet = {}
        self.depth = {}
        self.q = []
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        for i in wordList:
            self.wordSet[i] = 1
        if endWord not in self.wordSet:
            return 0
        self.depth[beginWord] = 1
        self.q.append(beginWord)
        while self.q:
            s = self.q[0]
            self.q = self.q[1:]
            for i in range(len(s)):
                for j in range(ord("a"),ord("z")+1):
                    c = chr(j)
                    if s[i] == c:
                        continue
                    ns = list(s)
                    ns[i] = c
                    ns = "".join(ns)
                    if ns not in self.wordSet:
                        continue
                    if ns in self.depth:
                        continue
                    self.depth[ns] = self.depth[s] + 1
                    self.q.append(ns)
                    if ns == endWord:
                        return self.depth[ns]
        return 0
