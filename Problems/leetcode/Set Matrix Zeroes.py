from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rowCheck, colCheck = [False for r in range(m)], [False for c in range(n)]

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rowCheck[r], colCheck[c] = True, True
        
        for r in range(m):
            if rowCheck[r]:
                for c in range(n):
                    matrix[r][c] = 0
        
        for c in range(n):
            if colCheck[c]:
                for r in range(m):
                    matrix[r][c] = 0
