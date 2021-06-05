import sys

M = 1000000000
length = [3]
side = [0]
i = 4
while(length[len(side) - 1] <= M):
    side.append(length[len(length) - 1])
    length.append(side[len(side) - 1] + i + side[len(side) - 1])
    i += 1

N = int(input())
idx = 0
while(length[idx] < N):
    idx += 1

def find(N:int, idx:int):
    if idx == 0:
        if N == 1:
            print("m")
        else:
            print("o")
        return

    if N <= side[idx]:
        find(N, idx - 1)
    elif N < length[idx] - side[idx]:
        if N - side[idx] == 1:
            print("m")
        else:
            print("o")
    else:
        find(N - side[idx] - (3 + idx), idx - 1)

find(N, idx)
