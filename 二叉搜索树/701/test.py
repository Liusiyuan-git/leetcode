# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root, val: int):
        return self.bst(root, val)

    def bst(self, node, val):
        if not node:
            return TreeNode(val)
        if node.val > val:
            node.left = self.bst(node.left, val)
        else:
            node.right = self.bst(node.right, val)
        return node
