import sys

T = int(sys.stdin.readline())
for t in range(T):
    n, m = map(int, sys.stdin.readline().split())
    conn = [[] for i in range(n+1)]

    for conn_info in range(m):
        x, y = map(int, sys.stdin.readline().split())
        conn[x].append(y)
        conn[y].append(x)
    
    check = [0 for i in range(n+1)]

    def dfs(node:int, color:int):
        if check[node] == 0:
            check[node] = color
            for nextNode in conn[node]:
                temp = dfs(nextNode, 3-color)
                if not temp:
                    return False
        else:
            if check[node] != color:
                return False
        return True
    
    result = True
    for node in range(1, n+1):
        if check[node] == 0:
            temp = dfs(node, 1)
            if not temp:
                result = False
                break
    
    print('possible' if result else 'impossible')
