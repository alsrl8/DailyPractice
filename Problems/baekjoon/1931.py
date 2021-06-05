import sys
N = int(sys.stdin.readline())
info = [list(map(int, sys.stdin.readline().split())) for i in range(N)] # [start, end]

info.sort(key=lambda x:[x[1],x[0]])
cnt = 0
endTime = 0
for i in range(N):
    if endTime <= info[i][0]:
        cnt += 1
        endTime = info[i][1]
print(cnt)
