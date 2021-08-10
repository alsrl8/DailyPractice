from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        answer = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                answer += 1
        return answer
