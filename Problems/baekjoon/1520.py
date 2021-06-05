import sys

sys.setrecursionlimit(50000)
M, N = map(int, sys.stdin.readline().split()) # M:세로, N:가로
S = []
for i in range(M):
    S.append(list(map(int, sys.stdin.readline().split())))

INF = 501 * 501
DP = [[INF for i in range(N)] for j in range(M)]
dRow = [1, -1, 0, 0]
dCol = [0, 0, 1, -1]
def dfs(r:int, c:int) -> int:
    global M, N, S, dRow, dCol
    val = 0
    if r == M - 1 and c == N - 1:
        return 1
    if DP[r][c] < INF:
        return DP[r][c]
    for d in range(4):
        newR = r + dRow[d]
        newC = c + dCol[d]
        if newR >= M or newC >= N or newR < 0 or newC < 0:
            continue
        elif S[newR][newC] < S[r][c]:
            val += dfs(newR, newC)
    DP[r][c] = val
    return val

answer = dfs(0, 0)
print(answer)
