from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for r in range(9):
            check = [False for i in range(9)]
            for c in range(9):
                val = int(board[r][c])-1 if board[r][c] != '.' else '.'
                if val == '.':
                    continue
                elif check[val]:
                    return False
                check[val] = True
        
        # check col
        for c in range(9):
            check = [False for i in range(9)]
            for r in range(9):
                val = int(board[r][c])-1 if board[r][c] != '.' else '.'
                if val == '.':
                    continue
                elif check[val]:
                    return False
                check[val] = True
        
        # check sub-boxes
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                check = [False for i in range(9)]
                for r1 in range(3):
                    for c1 in range(3):
                        val = int(board[r+r1][c+c1])-1 if board[r+r1][c+c1] != '.' else '.'
                        if val == '.':
                            continue
                        elif check[val]:
                            return False
                        check[val] = True
        return True
