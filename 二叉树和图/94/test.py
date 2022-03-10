# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def inorderTraversal(self, root):
        self.search(root)
        return self.ans

    def search(self,node):
        if not node:
            return
        self.search(node.left)
        self.ans.append(node.val)
        self.search(node.right)