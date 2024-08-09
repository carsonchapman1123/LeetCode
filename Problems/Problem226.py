# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root

test = TreeNode(1)
test.left = TreeNode(2)
test.right = TreeNode(3)
test.left.left = TreeNode(4)
test.left.right = TreeNode(5)

ret = Solution().invertTree(test)
print ret.val
print ret.left.val
print ret.right.right.val