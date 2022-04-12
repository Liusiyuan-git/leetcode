class Node:
    def __init__(self):
        self.count = 0
        self.hashmap = {}
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, s):
        curr = self.root
        for i in s:
            if i not in curr.hashmap:
                curr.hashmap[i] = Node()
            curr = curr.hashmap[i]
        curr.count += 1
class Solution:
    def __init__(self):
        self.visit = None
        self.m = 0
        self.n = 0
        self.str = ""
        self.ans = set()

    def findWords(self, board, words):
        t = Trie()
        for word in words:
            t.insert(word)
        self.m = len(board)
        self.n = len(board[0])
        self.visit = [[False for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.visit[i][j] = True
                self.dfs(board, i, j ,t.root)
                self.visit[i][j] = False
        return list(self.ans)

    def dfs(self,board, x, y, curr):
        dx = [-1,0,0,1]
        dy = [0,-1,1,0]
        ch = board[x][y]
        if ch not in curr.hashmap:
            return False
        nextT = curr.hashmap[ch]
        self.str += ch
        if nextT.count > 0:
            self.ans.add(self.str)
        if len(nextT.hashmap.keys()) == 0:
            del curr.hashmap[ch]
            del nextT
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= self.m or ny >= self.n:
                    continue
                if self.visit[nx][ny]:
                    continue
                self.visit[nx][ny] = True
                self.dfs(board, nx, ny ,nextT)
                self.visit[nx][ny] = False
        self.str  = self.str[:-1]
