import sys
from collections import deque

N, M, k = map(int, sys.stdin.readline().split())
A = [0] + list(map(int, sys.stdin.readline().split()))
conn = [[] for _ in range(N+1)]
for i in range(M):
    v, w = map(int, sys.stdin.readline().split())
    conn[v].append(w)
    conn[w].append(v)

check = [False for _ in range(N+1)]
pay = 0
for stu in range(1, N+1):
    if check[stu]:
        continue
    
    q = deque()
    q.append(stu)
    check[stu] = True
    minPay = A[stu]

    while q:
        s = q.popleft()
        for nextStu in conn[s]:
            if check[nextStu]:
                continue
            q.append(nextStu)
            check[nextStu] = True
            minPay = min(minPay, A[nextStu])
    
    pay += minPay

print('Oh no' if k < pay else pay)
