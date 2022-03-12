# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.p = None
        self.q = None
        self.ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        self.dfs(root)
        return self.ans

    def dfs(self,root):
        if not root:
            return False,False
        leftResult = self.dfs(root.left)
        rightResult = self.dfs(root.right)
        result = [False,False]
        result[0] = leftResult[0] or rightResult[0] or root.val == self.p.val
        result[1] = leftResult[1] or rightResult[1] or root.val == self.q.val
        if result[0] and result[1] and not self.ans:
            self.ans = root
        return result