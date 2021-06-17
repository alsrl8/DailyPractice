from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        answer = 0
        for start in range(len(nums)):
            maximum = nums[start]
            for end in range(start, len(nums)):
                maximum = max(maximum, nums[end])
                if maximum > right:
                    break
                elif maximum < left:
                    continue
                answer += 1
        return answer
