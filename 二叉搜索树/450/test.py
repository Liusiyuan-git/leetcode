# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key: int):
        return self.delbst(root, key)

    def delbst(self, node, key):
        if not node:
            return None
        if node.val == key:
            if node.right:
                leftNode = self.getLeftNext(node.right)
                leftNode.left = node.left
                return node.right
            else:
                return node.left
        else:
            node.left = self.delbst(node.left, key)
            node.right = self.delbst(node.right,key)
        return node

    def getLeftNext(self, node):
        if node.left:
            return self.getLeftNext(node.left)
        else:
            return node