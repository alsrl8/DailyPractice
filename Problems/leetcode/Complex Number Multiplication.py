class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        idx1, idx2 = num1.index('+'), num2.index('+')
        real1, real2 = int(num1[:idx1]), int(num2[:idx2])
        img1, img2 = int(num1[idx1+1:len(num1)-1]), int(num2[idx2+1:len(num2)-1])
        
        real = real1 * real2 - img1 * img2
        img = real1 * img2 + real2 * img1
        return str(real) + "+" + str(img) + "i"
