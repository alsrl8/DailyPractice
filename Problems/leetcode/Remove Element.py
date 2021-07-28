from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            num = nums[i]
            if num == val:
                k += 1
                continue

            if k == 0:
                continue

            nums[i-k], nums[i] = nums[i], nums[i-k]
        
        return len(nums)-k
