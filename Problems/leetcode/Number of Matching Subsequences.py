from typing import List
import string
from bisect import bisect_right

class Solution:
    
    def isMatched(self, dic:dict, word:str) -> bool:
        idx = -1
        for ch in word:
            temp = bisect_right(dic[ch], idx)
            if temp == len(dic[ch]):
                return False
            idx = dic[ch][temp]
        return True

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        alphabet_list = list(string.ascii_lowercase)
        dic = dict()
        for alphabet in alphabet_list:
            dic.update({alphabet:[]})
        
        for i in range(len(s)):
            ch = s[i]
            dic[ch].append(i)
        
        answer = 0
        for word in words:
            if self.isMatched(dic, word):
                answer += 1

        return answer
