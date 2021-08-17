# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.count = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.search(root, root.val)
        return self.count

    def search(self, node: TreeNode, maxVal: int):
        if maxVal <= node.val:
            maxVal = node.val
            self.count += 1
        
        if node.left:
            self.search(node.left, maxVal)
        if node.right:
            self.search(node.right, maxVal)
