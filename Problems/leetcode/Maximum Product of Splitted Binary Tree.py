from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SumOfChildren:
    def __init__(self, left = None, right = None) -> None:
        self.leftSum = 0
        self.rightSum = 0
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.answer = 0
        self.total = 0

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sum_of_children = SumOfChildren()
        self.search(root, sum_of_children)
        self.total = root.val + sum_of_children.leftSum + sum_of_children.rightSum
        self.remove_edge(root, sum_of_children)
        MOD = int(1e9 + 7)
        return self.answer % MOD
        
    def remove_edge(self, node: TreeNode, sum_of_children: SumOfChildren):
        if node.left:
            temp = sum_of_children.leftSum * (self.total - sum_of_children.leftSum)
            self.answer = max(self.answer, temp)
            self.remove_edge(node.left, sum_of_children.left)
        if node.right:
            temp = sum_of_children.rightSum * (self.total - sum_of_children.rightSum)
            self.answer = max(self.answer, temp)
            self.remove_edge(node.right, sum_of_children.right)
        
    def search(self, node: TreeNode, sum_of_children: SumOfChildren) -> int:
        if node.left:
            sum_of_children.left = SumOfChildren()
            sum_of_children.leftSum += self.search(node.left, sum_of_children.left)
        if node.right:
            sum_of_children.right = SumOfChildren()
            sum_of_children.rightSum += self.search(node.right, sum_of_children.right)
        return node.val + sum_of_children.leftSum + sum_of_children.rightSum
