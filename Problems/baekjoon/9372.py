import sys

T = int(sys.stdin.readline())

for t in range(T):
    N, M = map(int, sys.stdin.readline().split())
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())

    print(N-1)
