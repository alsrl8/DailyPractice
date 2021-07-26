from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTree(self, nums: List[int], L: int, R: int) -> TreeNode:
        if L > R:
            return None
            
        mid = (L + R) // 2
        node = TreeNode(nums[mid])
        node.left = self.generateTree(nums, L, mid-1)
        node.right = self.generateTree(nums, mid+1, R)
        return node
        
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.generateTree(nums, 0, len(nums)-1)
