from typing import List

class Solution:
    def isProper(self, s: str) -> bool:
        cnt = 0
        for i in range(len(s)):
            if s[i] == "(":
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                return False
        if cnt != 0:
            return False
        else:
            return True

    def generateParenthesis(self, n: int) -> List[str]:
        List = [""]
        for i in range(n * 2):
            temp = []
            for s in List:
                temp.append(s + "(")
                temp.append(s + ")")
            List = temp

        answer = []
        for s in List:
            if self.isProper(s):
                answer.append(s)
        return answer

    def generateParenthesis_2(self, n: int) -> List[str]:
        
        def helper(left, right, n, curr, result):
            if n == 0:
                result.append(''.join(curr))
            if left:
                curr.append('(')
                helper(left-1, right, n, curr, result)
                curr.pop()
            if right > left:
                curr.append(')')
                helper(left, right-1, n-1, curr, result)
                curr.pop()
        result = []
        helper(n, n, n, [], result)
        return result
