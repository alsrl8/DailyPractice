import sys
import heapq

# input
N, K = map(int, sys.stdin.readline().split())
jewelry = []
for i in range(N):
    jewelry.append(list(map(int, sys.stdin.readline().split())))
bag = []
for i in range(K):
    bag.append(int(sys.stdin.readline()))

# sort
bag.sort()
jewelry.sort(key=lambda x: x[0])

pq = []

answer = 0
j = 0
for b in range(K):
    while j < len(jewelry) and jewelry[j][0] <= bag[b]:
        heapq.heappush(pq, (-jewelry[j][1]))
        j += 1
    if len(pq) == 0:
        continue        
    answer += (heapq.heappop(pq) * (-1))
print(answer)
