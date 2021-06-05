import sys

N = int(input()) # N <= 20, N is always even
S = [[[] for _ in range(N)] for _ in range(N)]
minDiff = 20001

#input
for i in range(N):
    S[i] = list(map(int,input().split(' ')))

def pick(start_list, link_list, idx):
    global N, minDiff
    if(idx == N):
        sum_start = 0
        sum_list= 0
        for i in range(N // 2):
            for j in range(N // 2):
                sum_start += (S[start_list[i]][start_list[j]])
                sum_list += (S[link_list[i]][link_list[j]])
        diff = sum_start - sum_list
        if(diff < 0):
            diff *= -1
        if(minDiff > diff):
            minDiff = diff            
    else:
        # start team
        if(len(start_list) < (N // 2)):
            start_list.append(idx)
            pick(start_list, link_list, idx+1)
            del start_list[len(start_list) - 1]
        if(len(link_list) < (N // 2)):
            link_list.append(idx)
            pick(start_list, link_list, idx+1)
            del link_list[len(link_list) - 1]

start_list = []
link_list = []
pick(start_list, link_list, 0)
print(minDiff)        
