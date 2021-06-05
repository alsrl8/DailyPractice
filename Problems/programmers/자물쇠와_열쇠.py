import sys
import copy

def isProperKey(S, M, N):
    for i in range(M - 1, M + N - 1):
        for j in range(M - 1, M + N - 1):
            if(S[i][j] != 1):
                return False
    return True

def rotateKey(key): # clockwise
    M = len(key)
    temp = copy.deepcopy(key)
    for i in range(M):
        for j in range(M):
            temp[i][j] = key[M - 1 -j][i]
    return temp

def solution(key, lock):
    N = len(lock)
    M = len(key)
    L = N + 2 * (M - 1)
    S = [[0 for i in range(L)] for j in range(L)]
    for i in range(N):
        for j in range(N):
            S[i + (M - 1)][j + (M - 1)] = lock[i][j]

    for R in range(4):
        for i in range(N + M):
            for j in range(N + M):
                temp = copy.deepcopy(S)
                for r in range(i, i + M):
                    if(r < M - 1 or r > N + M - 2):
                        continue
                    for c in range(j, j + M):
                        if(c < M - 1 or c > N + M - 2):
                            continue
                        S[r][c] += key[r - i][c - j]                
                if(isProperKey(S, M, N)):
                    return True
                S = temp
        key = rotateKey(key)
    return False
