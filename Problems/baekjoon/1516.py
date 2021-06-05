import sys
from collections import deque

N = int(sys.stdin.readline())
S = [0] + [list(map(int, sys.stdin.readline().split())) for i in range(N)]
MAX = 500 * 100000
minTime = [MAX for i in range(N+1)]

conn = [[] for i in range(N+1)]
ed = [0 for i in range(N+1)] # entry degree

for i in range(1, N+1):
    for j in range(1, len(S[i])-1):
        conn[S[i][j]].append(i)

for i in range(1, N+1):
    ed[i] = (len(S[i]) - 2)

cntCheck = 0
check = [0 for i in range(N+1)]
q = deque()

while cntCheck < N:
    for i in range(1, N+1):
        if ed[i] == 0 and check[i] == 0:
            pre = 0
            for j in range(1, len(S[i])-1):
                pre = max(pre, check[S[i][j]])
            q.append((i, S[i][0] + pre))
            cntCheck += 1

    while q:
        node, time = q.popleft()
        check[node] = time
        for i in conn[node]:
            ed[i] -= 1

for i in range(1, N+1):
    print(check[i])
