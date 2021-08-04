from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root == None:
            return []
        answer = []
        self.search(root, targetSum, answer, [])
        return answer

    def search(self, node: TreeNode, rest: int, answer: List[List[int]], path: List[int]) -> None:
        path.append(node.val)
        rest -= node.val
        if node.left == None and node.right == None:
            if rest == 0:
                answer.append(path)
            return

        if node.left:
            self.search(node.left, rest, answer, path.copy())
        if node.right:
            self.search(node.right, rest, answer, path.copy())
