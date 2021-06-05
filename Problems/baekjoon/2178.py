import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
MAP = [list(sys.stdin.readline().rstrip()) for i in range(N)]

dRow = [1, -1, 0, 0]
dCol = [0, 0, 1, -1]

q = deque()
q.append((0,0,1))
check = [[False for i in range(M)] for j in range(N)]
check[0][0] = True

while len(q) > 0:
    temp = q.popleft()
    if temp[0] == N-1 and temp[1] == M-1:
        print(temp[2])
        break
    for d in range(4):
        newR = temp[0] + dRow[d]
        newC = temp[1] + dCol[d]
        if newR < 0 or newC < 0 or newR >= N or newC >= M:
            continue
        if MAP[newR][newC] == '0' or check[newR][newC]:
            continue
        check[newR][newC] = True
        q.append((newR, newC, temp[2]+1))
