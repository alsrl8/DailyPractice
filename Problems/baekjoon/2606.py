import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
CONN = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    CONN[a].append(b)
    CONN[b].append(a)
    

q = deque()
q.append(1)
cnt = 0
check = [False for i in range(N+1)]
check[1] = True

while len(q) > 0:
    temp = q.popleft()
    for i in CONN[temp]:
        if check[i]:
            continue
        check[i] = True
        cnt += 1
        q.append(i)
print(cnt)
