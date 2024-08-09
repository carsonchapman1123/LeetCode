class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


testRoot = TreeNode(3)
testRoot.left = TreeNode(9)
testRoot.right = TreeNode(20)
testRoot.right.left = TreeNode(15)
testRoot.right.left = TreeNode(7)
print Solution().maxDepth(testRoot)
