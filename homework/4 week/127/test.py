class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        start = set()
        end = set()
        start.add(beginWord)
        end.add(endWord)
        wordSet.remove(endWord)
        length = 1
        while start:
            nextSet = set()
            for word in start:
                wordArry = list(word)
                for i in range(len(wordArry)):
                    old = wordArry[i]
                    for j in range(ord("a"), ord("z") + 1):
                        wordArry[i] = chr(j)
                        s = "".join(wordArry)
                        if s in end:
                            return length + 1
                        if s in wordSet:
                            nextSet.add(s)
                            wordSet.remove(s)
                    wordArry[i] = old
            if len(nextSet) < len(end):
                start = nextSet
            else:
                start = end
            if len(start) >= len(end):
                end = nextSet
            length += 1
        return 0
