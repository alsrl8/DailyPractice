class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        L, R = [], []
        dominoes = list(dominoes)

        for i in range(len(dominoes)):
            domino = dominoes[i]
            if domino == 'L':
                L.append(i)
            elif domino == 'R':
                R.append(i)
        
        while len(L) > 0 or len(R) > 0:
            temp = []
            lateConvert = []
            for i in L:
                if i == 0:
                    continue
                elif dominoes[i-1] == '.':
                    if i == 1:
                        dominoes[0] = 'L'
                    else:
                        if dominoes[i-2] == 'R':
                            continue
                        else:
                            lateConvert.append(i-1)
                            temp.append(i-1)
            
            L = temp

            temp = []
            for i in R:
                if i == len(dominoes) - 1:
                    continue
                elif dominoes[i+1] == '.':
                    if i == len(dominoes) - 2:
                        dominoes[-1] = 'R'
                    else:
                        if dominoes[i+2] == 'L':
                            continue
                        else:
                            dominoes[i+1] = 'R'
                            temp.append(i+1)
            
            R = temp
            
            for i in lateConvert:
                dominoes[i] = 'L'

        return ''.join(dominoes)
