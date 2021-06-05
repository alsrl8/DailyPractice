def solution(n:int, s:int, a:int, b:int, fares:list):
    INF = int(1e5) * 200 + 1
    MAP = [[INF for _ in range(n+1)] for _ in range(n+1)]
    
    for fare in fares:
        c, d, f = map(int, fare)
        MAP[c][d], MAP[d][c] = f, f
        MAP[c][c], MAP[d][d] = 0, 0
    
    # O(N^3)
    for node in range(1, n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                MAP[start][end] = min(MAP[start][end], MAP[start][node] + MAP[node][end])
    answer = MAP[s][a] + MAP[s][b]

    weight = MAP[s]
    
    for shared in range(1, n+1):
        distance = weight[shared] + MAP[shared][a] + MAP[shared][b]
        answer = min(answer, distance)

    return answer
