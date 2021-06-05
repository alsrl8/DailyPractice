import sys

N = int(sys.stdin.readline().rstrip())
S = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

DP = [[1001, 1001, 1001] for i in range(N)] # RGC
for i in range(3):
    DP[0][i] = S[0][i]

for i in range(1, N):
    DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + S[i][0]
    DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + S[i][1]
    DP[i][2] = min(DP[i-1][0], DP[i-1][1]) + S[i][2]

print(min(DP[N-1][0], min(DP[N-1][1], DP[N-1][2])))
