from typing import List
from collections import deque

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        sizes = [0, 0]
        
        num = 2
        for r in range(n):
            for c in range(n):
                if grid[r][c] != 1:
                    continue
                size = self.search_island(grid, r, c, num)
                sizes.append(size)
                num += 1

        max_size = max(sizes)

        dRow = [0, 0, 1, -1]
        dCol = [1, -1, 0, 0]
        for r in range(n):
            for c in range(n):
                islands_to_merge = set()
                if grid[r][c] != 0:
                    continue
                for d in range(4):
                    newR = r + dRow[d]
                    newC = c + dCol[d]
                    if newR < 0 or newC < 0 or newR >= n or newC >= n:
                        continue
                    elif grid[newR][newC] == 0:
                        continue
                    islands_to_merge.add(grid[newR][newC])

                size = 1
                for island in islands_to_merge:
                    size += sizes[island]
                max_size = max(max_size, size)
        
        return max_size

    def search_island(self, grid: List[List[int]], r: int, c: int, num: int) -> int:
        dRow = [0, 0, 1, -1]
        dCol = [1, -1, 0, 0]
        n = len(grid)
        
        queue = deque()
        queue.append((r, c))
        grid[r][c] = num
        SIZE = 1
        
        while queue:
            row, col = queue.popleft()
            for d in range(4):
                newR = row + dRow[d]
                newC = col + dCol[d]
                if newR < 0 or newC < 0 or newR >= n or newC >= n:
                    continue
                elif grid[newR][newC] != 1:
                    continue
                grid[newR][newC] = num
                queue.append((newR, newC))
                SIZE += 1

        return SIZE
