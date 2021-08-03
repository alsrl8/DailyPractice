from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp = []
        lastNum, cnt = -11, 0
        for num in nums:
            if num == lastNum:
                cnt += 1
            else:
                temp.append((lastNum, cnt))
                lastNum = num
                cnt = 1
        temp.append((lastNum, cnt))
        nums = temp[1:]

        size = len(nums)
        BINARY_MAX = int(pow(2, size))

        answer = []
        for binary in range(BINARY_MAX):
            self.add_to_answer(answer, binary, nums, 0, [])

        return answer

    def add_to_answer(self, answer: List[List[int]], binary: int, nums: List[int], idx: int, subset: List[List[int]]):
        if binary == 0:
            answer.append(subset)
            return

        code = binary % 2
        if code == 0:
            self.add_to_answer(answer, binary//2, nums, idx+1, subset)
        else:   # code == 1
            copied = subset.copy()
            for cnt in range(nums[idx][1]):
                copied = copied.copy()
                copied.append(nums[idx][0])
                self.add_to_answer(answer, binary//2, nums, idx+1, copied)
