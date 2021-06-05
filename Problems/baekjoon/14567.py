import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
MAP = [[] for i in range(N+1)]
cnt = [0 for i in range(N+1)]
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    MAP[A].append(B)
    cnt[B] += 1

q = deque()
check = [False for i in range(N+1)]
cntCheck = 0
answer = [0 for i in range(N+1)]

turn = 1
while cntCheck < N:
    for i in range(1, N+1):
        if cnt[i] == 0 and not check[i]:
            q.append(i)
            check[i] = True
    while q:
        temp = q.popleft()
        OUT = MAP[temp]
        while OUT:
            cnt[OUT.pop()] -= 1
        answer[temp] = turn
        cntCheck += 1
    turn += 1

for i in range(1, N+1):
    print(answer[i], end=' ')
