from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = defaultdict(list)
        for i in range(len(nums)):
            num_set[nums[i]].append(i)
        
        for i in range(len(nums)):
            num = nums[i]
            if num == target-num:
                if len(num_set[target-num]) == 2:
                    return [i, num_set[num][1]]
                else:
                    continue

            if len(num_set[target-num]) == 1:
                return [i, num_set[target-num][0]]
