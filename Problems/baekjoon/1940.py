import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))

S.sort()
L, R = 0, len(S)-1

answer = 0
while L < R:
    if S[L] + S[R] > M:
        R -= 1
    elif S[L] + S[R] < M:
        L += 1
    else: # S[L] + S[R] == M
        answer += 1
        L += 1
        R -= 1
print(answer)
