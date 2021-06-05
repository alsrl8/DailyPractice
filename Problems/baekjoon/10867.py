N = int(input())
S = list(map(int, input().split()))
S.sort()
print(S[0], end =' ')
for i in range(1, N):
    if S[i] != S[i-1]:
        print(S[i], end = ' ')
