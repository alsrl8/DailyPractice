import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
MAP = [list(sys.stdin.readline().rstrip()) for i in range(N)]
INF = N*M+1
check = [[[False, False] for i in range(M)] for j in range(N)]

dRow = [1, -1, 0, 0]
dCol = [0, 0, 1, -1]
q = deque()
q.append([0,0,1,False]) # r, c, step, isWallBroken
answer = -1

while len(q) > 0:
    temp = q.popleft()
    r, c, step, isWallBroken = temp[0], temp[1], temp[2], temp[3]
    if r == N-1 and c == M-1:
        answer = step
        break

    for d in range(4):
        newR = r + dRow[d]
        newC = c + dCol[d]
        if newR < 0 or newC < 0 or newR >= N or newC >= M:
            continue
        if isWallBroken:
            if MAP[newR][newC] == '1' or check[newR][newC][1]:
                continue
            check[newR][newC][1] = True
            q.append([newR, newC, step+1, True])
        else:
            if MAP[newR][newC] == '1':
                if check[newR][newC][1]:
                    continue
                check[newR][newC][1] = True
                q.append([newR, newC, step+1, True])
            else: # MAP[newR][newC] == '0'
                if check[newR][newC][0]:
                    continue
                check[newR][newC][0] = True
                q.append([newR, newC, step+1, False])

print(answer)
