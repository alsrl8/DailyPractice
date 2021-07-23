# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def search(self, node: TreeNode) -> int:
        val = node.val

        if node.left:
            leftVal = self.search(node.left)
            if leftVal == 0:
                node.left = None
            val += leftVal

        if node.right:
            rightVal = self.search(node.right)
            if rightVal == 0:
                node.right = None
            val += rightVal

        return val

    def pruneTree(self, root: TreeNode) -> TreeNode:
        self.search(root)
        return root
