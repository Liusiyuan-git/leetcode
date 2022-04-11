class Node:
    def __init__(self):
        self.count = 0
        self.hashmap = {}


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        self.find(word, True, False)

    def search(self, word: str) -> bool:
        return self.find(word, False, False)

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix, False, True)

    def find(self, s, isInsert, isPrefix):
        curr = self.root
        for i in s:
            if i not in curr.hashmap:
                if isInsert:
                    curr.hashmap[i] = Node()
                else:
                    return False
            curr = curr.hashmap[i]
        if isInsert:
            curr.count += 1
        if isPrefix:
            return True
        return curr.count > 0

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
