import sys

T = int(input())
for t in range(T):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline()
    cnt = 0
    for i in range(n - 1, -1, -1):
        if s[i:i+1] == ")":
            cnt += 1
        else:
            break
    if cnt > n // 2:
        print("Yes")
    else:
        print("No")
