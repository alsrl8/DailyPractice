import sys

sys.setrecursionlimit(50000)

n = int(sys.stdin.readline())
nodes = [[] for i in range(n + 1)]

for i in range(n - 1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    nodes[parent].append((child, weight))

answer = 0


def search(node: int):
    global answer

    weightList = []
    for child, weight in nodes[node]:
        weightList.append(weight + search(child))

    weightList.sort(reverse=True)
    if len(weightList) >= 2:
        answer = max(answer, weightList[0] + weightList[1])
    elif len(weightList) == 1:
        answer = max(answer, weightList[0])

    return 0 if len(weightList) == 0 else weightList[0]


search(1)
print(answer)
