from typing import List
from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        count = Counter(arr)
        
        for num in arr:
            if count[num] == 0:
                continue
            
            if num < 0:
                if count[num // 2] == 0:
                    return False
                count[num] -= 1
                count[num // 2] -= 1
            else:
                count[num] -= 1
                if count[num * 2] == 0:
                    return False
                count[num * 2] -= 1
        
        return True

    def canReorderDoubled_improved(self, arr: List[int]) -> bool:
        count = Counter(arr)

        for num in sorted(count, key=abs):
            if count[num] > count[num*2]:
                return False
            count[num*2] -= count[num]
        
        return True
