import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
W, V = [0 for i in range(N)], [0 for i in range(N)]
for i in range(N):
    W[i], V[i] = map(int, sys.stdin.readline().rstrip().split())

DP = [[0, 0] for i in range(100001)]
cur, pre = 0, 1

for i in range(N):
    w, v = W[i], V[i]
    for j in range(1, w):
        DP[j][cur] = DP[j][pre]
    for j in range(w, K+1):
        DP[j][cur] = max(DP[j][pre], DP[j-w][pre] + v)
    cur = pre
    pre = (cur + 1) % 2

print(DP[K][pre])
