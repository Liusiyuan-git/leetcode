# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def __init__(self):
        self.count = 0

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = []
        self.dfs(queue, root)
        return ",".join(queue)

    def dfs(self, queue, root):
        if not root:
            queue.append("null")
            return
        queue.append(str(root.val))
        self.dfs(queue, root.left)
        self.dfs(queue, root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = data.split(",")
        return self.Decodes(queue)

    def Decodes(self, queue):
        if queue[self.count] == "null":
            self.count += 1
            return
        root = TreeNode(int(queue[self.count]))
        self.count += 1
        root.left = self.Decodes(queue)
        root.right = self.Decodes(queue)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))