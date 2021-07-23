# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def search(self, node: TreeNode, nodes_to_be_removed: set) -> int:
        val = node.val

        if node.left:
            val += self.search(node.left, nodes_to_be_removed)
        if node.right:
            val += self.search(node.right, nodes_to_be_removed)

        if val == 0:
            nodes_to_be_removed.add(node)

        return val

    def remove(self, node: TreeNode, nodes_to_be_removed: set) -> None:
        if node.left:
            if nodes_to_be_removed.__contains__(node.left):
                node.left = None
            else:
                self.remove(node.left, nodes_to_be_removed)
        
        if node.right:
            if nodes_to_be_removed.__contains__(node.right):
                node.right = None
            else:
                self.remove(node.right, nodes_to_be_removed)

    def pruneTree(self, root: TreeNode) -> TreeNode:
        nodes_to_be_removed = set()
        self.search(root, nodes_to_be_removed)

        if nodes_to_be_removed.__contains__(root):
            return None
        
        self.remove(root, nodes_to_be_removed)
        return root
