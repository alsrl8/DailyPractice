from itertools import combinations
from collections import defaultdict

def solution(orders:list, course:list) -> list:
    answer = []

    for c in course:
        dic = defaultdict(int)
        for order in orders:
            temp = list(combinations(order, c))
            for comb in temp:
                combined = ''.join(sorted(comb))
                dic[combined] += 1
        
        maxFrequency = 0
        for key in dic.keys():
            maxFrequency = max(maxFrequency, dic[key])
        if maxFrequency < 2:
            continue
        
        for key in dic.keys():
            if dic[key] == maxFrequency:
                answer.append(key)
    
    answer.sort()
    return answer
