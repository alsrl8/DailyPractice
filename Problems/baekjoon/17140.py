import sys
from collections import defaultdict

# initialize
r, c, k = map(int, sys.stdin.readline().split())
A = [[0 for i in range(100)] for j in range(100)]
inputA = [list(map(int, sys.stdin.readline().split())) for i in range(3)]
for i in range(3):
    for j in range(3):
        A[i][j] = inputA[i][j]


def operation(arr):
    cntNum = defaultdict(int)
    for i in range(100):
        if arr[i] == 0:
            continue
        cntNum[arr[i]] += 1

    cntNumList = []
    for num, cnt in cntNum.items():
        cntNumList.append((num, cnt))
    cntNumList.sort(key=lambda x: (x[1], x[0]))

    newArr = []
    for i in range(len(cntNumList)):
        newArr.append(cntNumList[i][0])  # num
        newArr.append(cntNumList[i][1])  # cnt

    return newArr[:100]


def operationR(A):
    newA = [[0 for i in range(100)] for j in range(100)]

    for r in range(100):
        row = A[r]
        newRow = operation(row)

        for i in range(len(newRow)):
            newA[r][i] = newRow[i]

    return newA


def operationC(A):
    newA = [[0 for i in range(100)] for j in range(100)]

    for c in range(100):
        col = [0 for i in range(100)]
        for r in range(100):
            col[r] = A[r][c]

        newCol = operation(col)

        for r in range(len(newCol)):
            newA[r][c] = newCol[r]

    return newA


def get_length(A):
    lenR, lenC = 0, 0

    for c in range(100):
        while lenR < 100 and A[lenR][c] != 0:
            lenR += 1

    for r in range(100):
        while lenC < 100 and A[r][lenC] != 0:
            lenC += 1

    return (lenR, lenC)


answer = 0
while answer <= 100:
    if A[r-1][c-1] == k:
        break
    lenR, lenC = get_length(A)
    if lenR >= lenC:
        A = operationR(A)
    else:
        A = operationC(A)
    answer += 1

if answer > 100:
    answer = -1
print(answer)
