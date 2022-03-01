class Solution:
    def __init__(self):
        self.totMap = {}

    def findSubstring(self, s: str, words):
        tot = 0
        ans = []
        for i in words:
            tot += len(i)
            if i not in self.totMap:
                self.totMap[i] = 1
            else:
                self.totMap[i] += 1

        for i in range(0, len(s) - tot + 1):
            if self.valid(s[i:i + tot], words[0]):
                ans.append(i)
        return ans

    def valid(self, sub, word):
        l = len(word)
        tmpMap = {}
        for i in range(0, len(sub), l):
            s = sub[i:i + l]
            if s not in tmpMap:
                tmpMap[s] = 1
            else:
                tmpMap[s] += 1
        return self.totMap == tmpMap
