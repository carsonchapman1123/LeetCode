# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is not None and root.left.val >= root.val or root.right is not None and root.right.val <= root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

test = TreeNode(5)
test.left = TreeNode(1)
test.right = TreeNode(4)

print Solution().isValidBST(test)