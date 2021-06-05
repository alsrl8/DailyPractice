import sys
import copy
from collections import deque

def solution(relation):
    cntRow = len(relation)
    cntCol = len(relation[0])
    check = [False for i in range(1 << cntCol)]
    result = 0

    def do_check(idx:int):
        for i in range(idx, len(check)):
            if(idx & i == idx):
                check[i] = True

    def isCandidateKey(l:list):
        for row1 in range(cntRow - 1):
            for row2 in range(row1 + 1, cntRow):
                cntEqual = 0
                for i in range(len(l)):
                    col = l[i]
                    if(relation[row1][col] == relation[row2][col]):
                        cntEqual += 1
                    else:
                        continue
                if(cntEqual == len(l)):
                    return False
        return True

    queue = deque()    
    for i in range(cntCol):
        queue.append([i])
    while(len(queue) > 0):
        temp = queue.popleft()
        if isCandidateKey(temp):
            num = 0
            for i in range(len(temp)):
                num += (1 << temp[i])
            if check[num]:
                continue
            do_check(num)
            result += 1
        else:
            lastNum = temp[len(temp) -1]
            for i in range(lastNum + 1, cntCol):
                temp2 = copy.deepcopy(temp)
                temp2.append(i)
                num = 0
                for j in range(len(temp2)):
                    num += (1 << temp2[j])
                if(check[num]):
                    continue
                else:
                    queue.append(temp2)
    return result
