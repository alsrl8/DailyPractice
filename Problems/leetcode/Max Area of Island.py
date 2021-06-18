from typing import List

class Solution:
    def dfs(self, grid:List[List[int]], size:List, r:int, c:int):
        dRow = [1, -1, 0, 0]
        dCol = [0, 0, 1, -1]
        for d in range(4):
            newR = r + dRow[d]
            newC = c + dCol[d]
            if newR < 0 or newC < 0 or newR >= self.R or newC >= self.C:
                continue
            elif self.check[newR][newC]:
                continue
            elif grid[newR][newC] == 0:
                continue
            self.check[newR][newC] = True
            size[0] += 1
            self.dfs(grid, size, newR, newC)


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.R, self.C = len(grid), len(grid[0])
        self.check = [[False for c in range(self.C)] for r in range(self.R)]
        answer = 0
        
        for r in range(self.R):
            for c in range(self.C):
                if self.check[r][c] or grid[r][c] == 0:
                    continue
                self.check[r][c] = True
                size = [1]
                self.dfs(grid, size, r, c)
                answer = max(answer, size[0])
        return answer
