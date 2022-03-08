# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0
        leftval = self.minDepth(root.left)
        rightval = self.minDepth(root.right)
        if not leftval and not rightval:
            return 1
        elif not leftval and rightval:
            return rightval + 1
        elif leftval and not rightval:
            return leftval + 1
        else:
            return min(leftval, rightval) + 1
