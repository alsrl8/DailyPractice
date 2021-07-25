import sys

N, M = map(int, sys.stdin.readline().split())
S = set()
for i in range(N):
    S.add(sys.stdin.readline().rstrip())

answer = 0
for i in range(M):
    if S.__contains__(sys.stdin.readline().rstrip()):
        answer += 1
print(answer)
