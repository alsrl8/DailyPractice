from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [nums[0]]
        for i, num in enumerate(nums[1:]):
            if arr[-1] < num:
                arr.append(num)
            else:
                for j in range(len(arr)):
                    if arr[j] >= num:
                        arr[j] = num
                        break
        return len(arr)
