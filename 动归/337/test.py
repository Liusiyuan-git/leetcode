# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.f = {}

    def rob(self, root) -> int:
        self.f[None] = [0, 0]
        self.dfs(root)
        return max(self.f[root][0], self.f[root][1])

    def dfs(self, root):
        if not root:
            return
        self.f[root] = [0, 0]
        self.dfs(root.left)
        self.dfs(root.right)
        self.f[root][0] = max(self.f[root.left][0], self.f[root.left][1]) + max(self.f[root.right][0],
                                                                                self.f[root.right][1])
        self.f[root][1] = self.f[root.left][0] + self.f[root.right][0] + root.val
