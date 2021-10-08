from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        answer = 0

        # case that you're not gonna rob nums[0]
        maxVal = [0, nums[1], nums[2]]
        for i in range(3, len(nums)):
            num = nums[i]
            temp = max([maxVal[-1], maxVal[-2]+num, maxVal[-3]+num])
            maxVal.append(temp)

        answer = maxVal[-1]
        
        # case that you're gonna rob nums[0]
        maxVal = [nums[0], nums[0], nums[0] + nums[2]]
        for i in range(3, len(nums)-1):
            num = nums[i]
            temp = max([maxVal[-1], maxVal[-2] + num, maxVal[-3] + num])
            maxVal.append(temp)
        
        answer = max(answer, maxVal[-1])

        return answer
