import sys

N, M, K = map(int, input().split())

class FireBall:
    def __init__(self, m:int, s:int, d:int):
        self.m = m
        self.s = s
        self.d = d

FB = [[[] for c in range(N + 1)] for r in range(N + 1)]

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    FB[r][c].append(FireBall(m,s,d))

dRow = [-1,-1,0,1,1,1,0,-1]
dCol = [0,1,1,1,0,-1,-1,-1]

for k in range(K):
    FB_temp = [[[] for c in range(N + 1)] for r in range(N + 1)]
    
    # move
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            for i in range(len(FB[r][c])):
                newR = r + (FB[r][c][i].s * dRow[FB[r][c][i].d]) % N
                newC = c + (FB[r][c][i].s * dCol[FB[r][c][i].d]) % N
                newR = (newR + N) % N
                newC = (newC + N) % N
                if(newR == 0):
                    newR = N
                if(newC == 0):
                    newC = N
                
                FB_temp[newR][newC].append(FireBall(FB[r][c][i].m, FB[r][c][i].s, FB[r][c][i].d))
    
    # merge and split
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if(len(FB_temp[r][c]) > 1):
                m_temp = 0
                s_temp = 0
                cnt_d_odd = 0
                for i in range(len(FB_temp[r][c])):
                    m_temp += FB_temp[r][c][i].m
                    s_temp += FB_temp[r][c][i].s
                    if(FB_temp[r][c][i].d % 2 == 1):
                        cnt_d_odd += 1
                
                m_temp = m_temp // 5
                s_temp = s_temp // len(FB_temp[r][c])
                if cnt_d_odd == len(FB_temp[r][c]):
                    cnt_d_odd = 0
                
                if cnt_d_odd != 0:
                    cnt_d_odd = 1
                
                while len(FB_temp[r][c]) > 0:
                    del FB_temp[r][c][0]
                
                if m_temp == 0:
                    continue
                
                # split
                for i in range(4):
                    FB_temp[r][c].append(FireBall(m_temp, s_temp, i * 2 + cnt_d_odd))
    FB = FB_temp

total = 0
for r in range(1, N + 1):
    for c in range(1, N + 1):
        for i in range(len(FB[r][c])):
            total += FB[r][c][i].m
print(total)
