from typing import List

class Solution:
    def pick(self, cur: int, length: int, matchsticks: List[int], check: List[bool]) -> bool:
        if cur == length:
            return True

        for i in range(len(matchsticks)):
            if check[i]:
                continue
            elif matchsticks[i] + cur > length:
                continue
            else:
                check[i] = True
                if self.pick(cur + matchsticks[i], length, matchsticks, check):
                    return True
                check[i] = False
        return False


    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 > 0:
            return False
        
        length = total // 4
        
        matchsticks.sort(reverse=True)
        check = [False for i in range(len(matchsticks))]

        for i in range(4):
            if self.pick(0, length, matchsticks, check) == False:
                return False
        return True
