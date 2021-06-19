import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
MAP = [[0 for c in range(N)] for r in range(N)]
SWITCH = [[[] for c in range(N)] for r in range(N)]
for _ in range(M):
    x,y,a,b = map(int, sys.stdin.readline().split())
    SWITCH[x-1][y-1].append((a-1,b-1))

def explore():
    global MAP, SWITCH, N

    dRow = [0,0,1,-1]
    dCol = [1,-1,0,0]

    q = deque()
    q.append((0,0))
    check = [[False for c in range(N)] for r in range(N)]
    check[0][0] = True
    while q:
        r, c = q.popleft()
        for switch in SWITCH[r][c]:
            MAP[switch[0]][switch[1]] = 1
        for d in range(4):
            newR = r + dRow[d]
            newC = c + dCol[d]
            if newR < 0 or newR >= N or newC < 0 or newC >= N:
                continue
            elif MAP[newR][newC] == 0:
                continue
            elif check[newR][newC]:
                continue
            q.append((newR, newC))
            check[newR][newC] = True

def countLightedRooms() -> int:
    global MAP, N
    cnt = 0
    for r in range(N):
        for c in range(N):
            if MAP[r][c] > 0:
                cnt += 1
    return cnt

MAP[0][0] = 1
answer = 0
temp = countLightedRooms()
while temp != answer:
    answer = temp
    explore()
    temp = countLightedRooms()

print(answer)
