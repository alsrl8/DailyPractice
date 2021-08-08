import sys

# input
N = int(sys.stdin.readline())
parents_info = list(map(int, sys.stdin.readline().split()))
remove = int(sys.stdin.readline())

root = 0
for node in range(N):
    if parents_info[node] == -1:
        root = node

children_info = [[] for i in range(N)]
for i in range(N):
    parent = parents_info[i]
    if parent >= 0:
        children_info[parent].append(i)

# remove node
parent = parents_info[remove]
if remove != root:
    children_info[parent].remove(remove)

answer = 0
def dfs(node:int):
    global answer

    if len(children_info[node]) == 0:
        answer += 1
        return

    for child in children_info[node]:
        dfs(child)

dfs(root)
print(answer if remove != root else 0)
