from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for s in strs:
            key = tuple(sorted(s))
            dic[key] = dic.get(key, []) + [s]
        return dic.values()
