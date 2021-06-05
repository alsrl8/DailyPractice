import sys

# input
N = int(sys.stdin.readline())
price = list(map(int, sys.stdin.readline().split()))
money = int(sys.stdin.readline())

S = ["" for i in range(51)] # S[i] is maximum number you can buy with money 'i'
for i in range(N):
    S[price[i]] = str(i)

def findMaximum(p:int):
    if S[p] == "":
        return
    for num in range(N):
        if p + price[num] > money:
            continue
        elif S[p + price[num]] == '':
            S[p + price[num]] = S[p] + str(num)
            continue    
        elif int(S[p + price[num]]) >= int(S[p] + str(num)):
            continue
        S[p + price[num]] = S[p] + str(num)

for i in range(1, money + 1):
    findMaximum(i)

answer = 0
for i in range(money + 1):
    if S[i] == '':
        continue
    answer = max(answer, int(S[i]))
print(answer)
