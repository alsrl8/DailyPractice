import sys
from math import ceil, log2

N, M, K = map(int, sys.stdin.readline().split())
num = [int(sys.stdin.readline()) for i in range(N)]
cmd = [list(map(int, sys.stdin.readline().split())) for i in range(M+K)]
h = ceil(log2(N))
l = (1 << (h+1))
tree = [0 for i in range(l)]

def init(start:int, end:int, node:int) -> int:
    global tree, num
    if start == end:
        tree[node] = num[start]
        return tree[node]

    mid = (start+end)//2
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return tree[node]

def getSum(L:int, R:int, start:int, end:int, node:int) -> int:
    global tree
    if L <= start and end <= R:
        return tree[node]
    elif R < start or end < L:
        return 0
    else:
        mid = (start+end)//2
        return getSum(L, R, start, mid, node*2) + getSum(L, R, mid+1, end, node*2+1)

def update(idx:int, diff:int, start:int, end:int, node:int):
    global tree
    if idx < start or idx > end:
        return
    
    tree[node] += diff
    if start == end:
        return
    else:
        mid = (start+end)//2
        update(idx, diff, start, mid, node*2)
        update(idx, diff, mid+1, end, node*2+1)

init(0, N-1, 1)
for i in range(M+K):
    a, b, c = cmd[i][0], cmd[i][1], cmd[i][2]
    if a == 1: # update
        diff = c - num[b-1]
        update(b-1, diff, 0, N-1, 1)
        num[b-1] = c
    else: # a == 2, getSum
        print(getSum(b-1, c-1, 0, N-1, 1))
