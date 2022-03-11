# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.preorder = None
        self.inorder = None
    def buildTree(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        return self.build(0, len(preorder) - 1, 0, len(inorder) - 1)

    def build(self, l1,r1,l2,r2):
        if l1 > r1:
            return None
        root = TreeNode(self.preorder[l1])
        mid = l2
        while self.inorder[mid] != root.val:
            mid += 1
        root.left = self.build(l1 + 1, l1 + mid - l2, l2 , mid - 1)
        root.right = self.build(l1 + mid - l2 + 1, r1, mid + 1, r2)
        return root