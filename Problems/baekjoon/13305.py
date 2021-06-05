import sys

N = int(sys.stdin.readline())
dis = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

answer = 0
minCost = cost[0]

for i in range(N-1):
    minCost = min(minCost, cost[i])
    answer += minCost * dis[i]
print(answer)
