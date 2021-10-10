from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = max(nums)
        n = len(nums)
        P, N = [0 for i in range(n)], [0 for i in range(n)]
        if nums[0] > 0:
            P[0] = nums[0]
        else:
            N[0] = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if num == 0:
                continue
            elif num > 0:
                P[i] = P[i-1] * num if P[i-1] != 0 else num
                N[i] = N[i-1] * num if N[i-1] != 0 else 0
                if P[i] != 0:
                    answer = max(answer, P[i])
            else:
                N[i] = P[i-1] * num if P[i-1] != 0 else num
                P[i] = N[i-1] * num if N[i-1] != 0 else 0
                if P[i] != 0:
                    answer = max(answer, P[i])

        return answer
