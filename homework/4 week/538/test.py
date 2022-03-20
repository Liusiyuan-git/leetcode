# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []  # 定义全局变量， 保存遍历结果

    def convertBST(self, root):
        head = root  # 定义根节点，方便返回
        self.search(root)  # 中序遍历
        self.ans.reverse()  # 将结果数组翻个个儿，便于遍历
        for i in range(0, len(self.ans)):
            if i > 0:
                self.ans[i].val += self.ans[i - 1].val  # 求前缀和，便是最终答案
        return head

    def search(self, node):  # 中序遍历
        if not node:
            return
        self.search(node.left)
        self.ans.append(node)
        self.search(node.right)
