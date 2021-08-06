from typing import List
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        answer = []
        if not root:
            return answer
        
        q = deque()
        q.append((root, 0))
        while q:
            node, level = q.popleft()
            if len(answer) == level:
                answer.append([node.val])
            else:
                answer[level].append(node.val)

            for child in node.children:
                q.append((child, level + 1))

        return answer
