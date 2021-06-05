import sys
from bisect import bisect_left

N, K = map(int, sys.stdin.readline().split())
X = [int(sys.stdin.readline()) for i in range(N)]

X.sort()
L, R = 1, X[-1] + K

answer = 0
while L <= R:
    mid = (L + R) // 2
    idx = bisect_left(X, mid)
    SUM = mid * idx - sum(X[:idx])
    if SUM <= K:
        answer = max(answer, mid)
        L = mid + 1
    else:
        R = mid - 1

print(answer)
