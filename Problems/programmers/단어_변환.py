import sys
from collections import deque

def isChangeable(str1:str, str2:str) -> bool:
    cnt = 0
    for i in range(len(str1)):
        if str1[i:i+1] == str2[i:i+1]:
            cnt +=1
    if cnt == len(str1) - 1:
        return True
    else:
        return False

def solution(begin:str, target:str, words:list) -> int:
    l = len(begin)
    if not words.__contains__(target):
        return 0
    
    dic = dict()
    dic.update({begin:[]})
    for i in range(len(words)):
        if isChangeable(begin, words[i]):
            dic[begin].append(words[i])

    for i in range(len(words)):
        if dic.__contains__(words[i]):
            continue
        dic.update({words[i]:[]})
        for j in range(len(words)):
            if i == j:
                continue
            if isChangeable(words[i], words[j]):
                dic[words[i]].append(words[j])
    
    queue = deque()
    wordIndex = dict()
    for i in range(len(words)):
        wordIndex.update({words[i]:i})
    check = [0 for i in range(len(words))]

    for i in range(len(dic[begin])):
        queue.append(dic[begin][i])
        check[wordIndex[dic[begin][i]]] = 1
        
    while len(queue) > 0:
        temp = queue.popleft()
        if temp == target:
            return check[wordIndex[target]]
        for i in range(len(dic[temp])):
            if check[wordIndex[dic[temp][i]]] > 0:
                continue
            check[wordIndex[dic[temp][i]]] = check[wordIndex[temp]] + 1
            queue.append(dic[temp][i])
    
    return 0
