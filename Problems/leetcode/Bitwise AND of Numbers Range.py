class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left, right = self.convert_to_bitwise(left), self.convert_to_bitwise(right)
        if len(left) != len(right):
            return 0

        answer = 0
        for i in range(len(right)):
            if right[i] == '1':
                if left[i] == '0':
                    break
                else:
                    answer += 2**(len(right)-1-i)
        return answer

    def convert_to_bitwise(self, num: int) -> str:
        bit = []
        while num > 0:
            if num & 1:
                bit.append('1')
            else:
                bit.append('0')
            num = num >> 1
        return ''.join(reversed(bit))
