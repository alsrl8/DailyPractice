from typing import List
from collections import defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1

        nums = sorted(list(set(nums)))
        
        dp = [[0, 0]] # picked, passed
        lastNum = -1
        for i, num in enumerate(nums):
            if num == lastNum + 1:
                picked = dp[-1][1] + dic[num] * num
                passed = max(dp[-1][0], dp[-1][1])
                dp.append([picked, passed])
            else:
                picked = max(dp[-1][0], dp[-1][1]) + dic[num] * num
                passed = max(dp[-1][0], dp[-1][1])
                dp.append([picked, passed])
            lastNum = num
        return max(dp[-1])
