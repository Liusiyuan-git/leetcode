# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        self.reverse(root)
        return root
    def reverse(self, root):
        if not root:
            return
        t = root.left
        root.left = root.right
        root.right = t
        self.reverse(root.left)
        self.reverse(root.right)