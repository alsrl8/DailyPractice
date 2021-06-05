import sys

sys.setrecursionlimit(40000)

n = int(input())
bamboo = []
for i in range(n):
    bamboo.append(list(map(int, input().split())))

DP = [[0 for i in range(n)] for j in range(n)]
dRow = [1, -1, 0, 0]
dCol = [0, 0, 1, -1]


def dfs(row: int, col: int):
    global DP, bamboo, n

    if DP[row][col] > 0:
        return DP[row][col]

    DP[row][col] = 1

    for d in range(4):
        newR = row + dRow[d]
        newC = col + dCol[d]
        if newR < 0 or newC < 0 or newR >= n or newC >= n:
            continue
        if bamboo[newR][newC] <= bamboo[row][col]:
            continue
        DP[row][col] = max(DP[row][col], dfs(newR, newC) + 1)
    return DP[row][col]


M = 0
for i in range(n):
    for j in range(n):
        if DP[i][j] == 0:
            M = max(M, dfs(i, j))
print(M)
