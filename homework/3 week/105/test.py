# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        self.preorder = preorder
        self.index = 0
        self.mp = {}
        for i in range(len(inorder)):
            self.mp[inorder[i]] = i
        return self.build(0, len(preorder) - 1)

    def build(self, l, r):
        if l > r or self.index == len(self.preorder):
            return None
        rootIndex = self.mp[self.preorder[self.index]]
        if rootIndex < l or r < rootIndex:
            return None
        root = TreeNode(self.preorder[self.index])
        self.index += 1
        root.left = self.build(l, rootIndex - 1)
        root.right = self.build(rootIndex+1, r)
        return root