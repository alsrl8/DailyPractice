from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        MAX = arr[-1]
        arr[-1] = -1
        idx = len(arr) - 2
        while idx >= 0:
            temp = arr[idx]
            arr[idx] = MAX
            MAX = max(MAX, temp)
            idx -= 1
        return arr
            
