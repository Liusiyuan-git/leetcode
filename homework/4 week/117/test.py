"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        while queue:
            n = []
            for i in queue:
                if i.left:
                    n.append(i.left)
                if i.right:
                    n.append(i.right)
            for i in range(len(n)):
                if i > 0:
                    n[i - 1].next = n[i]
            queue = n
        return root
