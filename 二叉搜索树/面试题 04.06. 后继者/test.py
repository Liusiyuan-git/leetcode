# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root, p):
        return self.getNext(root, p.val)


    def getNext(self, root, val):
        ans = None
        curr = root
        while curr:
            if curr.val == val:
                if curr.right:
                    ans = curr.right
                    while ans.left:
                        ans = ans.left
                break
            if val < curr.val:
                if not ans or ans.val > curr.val:
                    ans = curr
                curr = curr.left
            else:
                curr = curr.right
        return ans
