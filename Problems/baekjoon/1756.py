D, N = map(int, input().split())
dia = list(map(int, input().split()))
dow = list(map(int, input().split()))

minDia = []
m = dia[0]
for i in range(D):
    m = min(m, dia[i])
    minDia.append(m)

i, d = 0, D-1
answer = -1
while True:
    if minDia[d] >= dow[i]:
        i += 1
    d -= 1
    if i == N:
        answer = d + 1
        break
    elif d < 0:
        break

print(answer + 1)
