from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.nums = set()
        self.answer = False

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.search(root, k)
        return self.answer

    def search(self, node: TreeNode, k: int):
        if self.nums.__contains__(k - node.val):
            self.answer = True
            return
        
        self.nums.add(node.val)
        
        if node.left:
            self.search(node.left, k)
        if node.right:
            self.search(node.right, k)
