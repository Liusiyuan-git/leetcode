# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.postorder = None
        self.inorder = None

    def buildTree(self, inorder, postorder):
        postorder.reverse()  # 后序遍历都是最后的为根，所以跟着倒个个儿，这样第一个元素就为根，符合思维习惯
        inorder.reverse()  # 中序也跟着倒个个儿, 方便后面拆分
        self.postorder = postorder  # 定义全局postorder
        self.inorder = inorder  # 定义全局inorder
        return self.build(0, len(postorder) - 1, 0, len(inorder) - 1)

    def build(self, l1, r1, l2, r2):
        if l1 > r1:
            return None
        root = TreeNode(self.postorder[l1])
        mid = l2
        while self.inorder[mid] != root.val: #找到 中序点mid
            mid += 1
        root.right = self.build(l1 + 1, l1 + mid - l2, l2, mid - 1) # 找到中序点后，已此为中心进行划分，左边是右子树，右边是左子树，跟前序相反
        root.left = self.build(l1 + mid - l2 + 1, r1, mid + 1, r2)
        return root
