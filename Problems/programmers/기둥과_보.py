def solution(n, build_frame):
    S = [[[] for c in range(n + 1)] for r in range(n + 1)]
    
    def isProper():
        for x in range(n + 1):
            for y in range(n + 1):
                if S[x][y].__contains__(0) and y > 0: # pillar (y < n)
                    if not S[x][y - 1].__contains__(0) and not S[x][y].__contains__(1) and ((x > 0 and not S[x - 1][y].__contains__(1)) or x == 0):
                        return False
                if S[x][y].__contains__(1): # panel (x < n, y > 0)
                    if not S[x][y - 1].__contains__(0) and not S[x + 1][y - 1].__contains__(0) and ((x == 0 and not S[x + 1][y].__contains__(1)) or (x == n-1 and not S[x - 1][y].__contains__(1)) or (not S[x - 1][y].__contains__(1) or not S[x + 1][y].__contains__(1))):
                        return False
        return True
        
    for iCmd in range(len(build_frame)):
        x, y, a, b = build_frame[iCmd][0], build_frame[iCmd][1], build_frame[iCmd][2], build_frame[iCmd][3]
        if b == 1:
            S[x][y].append(a)
            if not isProper():
                S[x][y].remove(a)
        else:
            S[x][y].remove(a)
            if not isProper():
                S[x][y].append(a)

    answer = []
    for x in range(n + 1):
        for y in range(n + 1):
            if S[x][y].__contains__(0):
                answer.append([x, y, 0])
            if S[x][y].__contains__(1):
                answer.append([x, y, 1])

    return answer
