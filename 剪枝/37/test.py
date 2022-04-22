class Solution:
    def __init__(self):
        self.row = [[False for _ in range(10)] for _ in range(9)]
        self.col = [[False for _ in range(10)] for _ in range(9)]
        self.box = [[False for _ in range(10)] for _ in range(9)]

    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for digit in range(1, 10):
                self.row[i][digit] = self.col[i][digit] = self.box[i][digit] = True
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                digit = ord(board[i][j]) - ord("0")
                self.row[i][digit] = False
                self.col[j][digit] = False
                self.box[self.boxIndex(i, j)][digit] = False
        self.dfs(board)

    def dfs(self, board):

        pos = self.findMinimumProbability(board)
        x = pos[0]
        y = pos[1]
        if x == -1:
            return True
        avalibaleDigits = self.getAvalibaleDigits(x, y)
        for digit in avalibaleDigits:
            board[x][y] = chr(ord("0") + digit)
            self.row[x][digit] = False
            self.col[y][digit] = False
            self.box[self.boxIndex(x, y)][digit] = False
            if self.dfs(board):
                return True
            self.row[x][digit] = True
            self.col[y][digit] = True
            self.box[self.boxIndex(x, y)][digit] = True
            board[x][y] = "."
        return False

    def findMinimumProbability(self, board):
        minValue = 10
        pos = [-1, -1]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    continue
                avalibaleDigits = self.getAvalibaleDigits(i, j)
                if len(avalibaleDigits) < minValue:
                    minValue = len(avalibaleDigits)
                    pos = [i, j]
        return pos

    def getAvalibaleDigits(self, i, j):
        avalibaleDigits = []
        for digit in range(1, 10):
            if self.row[i][digit] and self.col[j][digit] and self.box[self.boxIndex(i, j)][digit]:
                avalibaleDigits.append(digit)
        return avalibaleDigits

    def boxIndex(self, i, j):
        return (i // 3) * 3 + j // 3