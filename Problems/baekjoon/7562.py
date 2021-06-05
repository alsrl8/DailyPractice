import sys
from collections import deque

T = int(sys.stdin.readline())
for t in range(T):
    I = int(sys.stdin.readline())
    R, C = map(int, sys.stdin.readline().split())
    R2, C2 = map(int, sys.stdin.readline().split())

    q = deque()
    q.append((R,C,0))
    INF = 1e9
    check = [[False for i in range(I)] for j in range(I)]
    check[R][C] = True
    dRow = [-2, -1, 1, 2, 2, 1, -1, -2]
    dCol = [1, 2, 2, 1, -1, -2, -2, -1]

    while len(q) > 0:
        temp = q.popleft()
        if temp[0] == R2 and temp[1] == C2:
            print(temp[2])
            break
        for d in range(8):
            newR = temp[0]+dRow[d]
            newC = temp[1]+dCol[d]
            if newR < 0 or newC < 0 or newR >= I or newC >= I:
                continue
            if check[newR][newC]:
                continue
            check[newR][newC] = True
            q.append((newR,newC,temp[2]+1))
