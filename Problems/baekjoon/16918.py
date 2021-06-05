import sys
from collections import deque

R, C, N = map(int, sys.stdin.readline().split())
MAP = [list(sys.stdin.readline().rstrip()) for i in range(R)]
for r in range(R):
    for c in range(C):
        if MAP[r][c] == 'O':
            MAP[r][c] = 1
        else:
            MAP[r][c] = 0
time = 0

def explode():
    global MAP, R, C
    dRow = [0, 0, 1, -1]
    dCol = [1, -1, 0, 0]
    q = deque()
    for r in range(R):
        for c in range(C):
            if MAP[r][c] > 3:
                q.append((r,c))
                for d in range(4):
                    newR = r + dRow[d]
                    newC = c + dCol[d]
                    if newR < 0 or newR >= R or newC < 0 or newC >= C:
                        continue
                    q.append((newR, newC))
    while q:
        r, c = q.popleft()
        MAP[r][c] = 0
    

def setBombs():
    global MAP, R, C
    for r in range(R):
        for c in range(C):
            if MAP[r][c] == 0:
                MAP[r][c] = 1

def timeFlows():
    global MAP, R, C
    for r in range(R):
        for c in range(C):
            if MAP[r][c] > 0:
                MAP[r][c] += 1

step = 0
while time < N:
    if step == 0:
        timeFlows()
        step = 1
    elif step == 1:
        timeFlows()
        setBombs()
        step = 2
    elif step == 2:
        timeFlows()
        explode()
        step = 1
    time += 1

for r in range(R):
    for c in range(C):
        if MAP[r][c] == 0:
            print('.', end='')
        else:
            print('O', end='')
    print('')
