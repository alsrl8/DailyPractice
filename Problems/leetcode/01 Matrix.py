from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        MAX_DISTANCE = m * n
        visited = [[MAX_DISTANCE for _ in range(n)] for _ in range(m)]
        q = deque()

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c, 0))
                    visited[r][c] = 0

        dRow = [0, 0, 1, -1]
        dCol = [1, -1, 0, 0]
        while q:
            r, c, dis = q.popleft()
            for d in range(4):
                newR = r + dRow[d]
                newC = c + dCol[d]
                if newR < 0 or newC < 0 or newR >= m or newC >= n:
                    continue
                elif visited[newR][newC] <= dis + 1:
                    continue
                
                visited[newR][newC] = dis + 1
                q.append((newR, newC, dis+1))
                
        return visited
