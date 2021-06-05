import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
S = [[] for i in range(N+1)]
for i in range(M):
    fr, to = map(int, sys.stdin.readline().split())
    S[fr].append(to)

answer = []
q = deque()
q.append((X, 0))
check = [False for i in range(N+1)]
check[X] = True
while len(q) > 0:
    temp = q.popleft()
    if temp[1] == K:
        answer.append(temp[0])
        continue
    for i in range(len(S[temp[0]])):
        city = S[temp[0]][i]
        if check[city]:
            continue
        check[city] = True
        q.append((city, temp[1] + 1))

if len(answer) > 0:
    answer.sort()
    for i in range(len(answer)):
        print(answer[i])
else:
    print(-1)
