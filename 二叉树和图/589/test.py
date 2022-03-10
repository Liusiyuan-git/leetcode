"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def __init__(self):
        self.ans = []

    def preorder(self, root: 'Node'):
        self.search(root)
        return self.ans

    def search(self, node):
        if not node:
            return
        self.ans.append(node.val)
        for i in node.children:
            self.search(i)
