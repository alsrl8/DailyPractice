import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
S = [[False for i in range(N+1)] for j in range(N+1)]
for i in range(M):
    p1, p2 = map(int, sys.stdin.readline().split())
    S[p1][p2] = True
    S[p2][p1] = True

answer = (0, 101 * 101)

INF = 101
for p in range(1, N+1):
    dis = [INF for i in range(N+1)]
    q = deque()
    q.append((p, 0))

    while len(q) > 0:
        temp = q.popleft()
        dis[temp[0]] = temp[1]
        for i in range(1, N+1):
            if not S[temp[0]][i]:
                continue
            if dis[i] > temp[1] + 1:
                q.append((i, temp[1] + 1))
    
    sumDis = 0
    for i in range(1, N+1):
        sumDis += dis[i]

    if sumDis < answer[1]:
        answer = (p, sumDis)

print(answer[0])
