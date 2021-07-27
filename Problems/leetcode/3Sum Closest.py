from typing import List
from bisect import bisect_left

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = sum(nums[:3])

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                find = target - (nums[i] + nums[j])
                idx = bisect_left(nums, find, lo=j+1)

                if idx - 1 > j:
                    if abs(answer - target) > abs(nums[idx-1] + nums[i] + nums[j] - target):
                        answer = nums[idx-1] + nums[i] + nums[j]

                if idx < len(nums):
                    if abs(answer - target) > abs(nums[idx] + nums[i] + nums[j] - target):
                        answer = nums[idx] + nums[i] + nums[j]
        return answer
