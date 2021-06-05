from itertools import permutations

def get_distance(board:list, r1:int, c1:int, r2:int, c2:int) -> int:
    dis1 = get_col_distance(board, r1, c1, c2) + get_row_distance(board, r1, r2, c2)
    dis2 = get_col_distance(board, r2, c1, c2) + get_row_distance(board, r1, r2, c1)
    return min(dis1, dis2)

def get_col_distance(board:list, r:int, c1:int, c2:int) -> int:
    if c1 < c2:
        diff = c2 - c1
        if diff <= 1:
            return diff
        elif diff == 2:
            return 2 if board[r][c1+1] > 0 or (c2 < 3 and board[r][c2] == 0) else 1
        else:   # diff == 3
            if board[r][c1+1] > 0:
                return 3 if board[r][c1+2] > 0 else 2
            else:
                return 2 if board[r][c1+2] > 0 else 1
    else:
        diff = c1 - c2
        if diff <= 1:
            return diff
        elif diff == 2:
            return 2 if board[r][c2+1] > 0 or (c2 > 0 and board[r][c2] == 0) else 1
        else:   # diff == 3
            if board[r][c2+1] > 0:
                return 3 if board[r][c2+2] > 0 else 2
            else:
                return 2 if board[r][c2+2] > 0 else 1

def get_row_distance(board:list, r1:int, r2:int, c:int) -> int:
    if r1 < r2:
        diff = r2 - r1
        if diff <= 1:
            return diff
        elif diff == 2:
            return 2 if board[r1+1][c] > 0 or (r2 < 3 and board[r2][c] == 0) else 1
        else:   # diff == 3
            if board[r1+1][c] > 0:
                return 3 if board[r1+2][c] > 0 else 2
            else:
                return 2 if board[r1+2][c] > 0 else 1
    else:
        diff = r1 - r2
        if diff <= 1:
            return diff
        elif diff == 2:
            return 2 if board[r2+1][c] > 0 or (r2 > 0 and board[r2][c] == 0) else 1
        else:   # diff == 3
            if board[r2+1][c] > 0:
                return 3 if board[r2+2][c] > 0 else 2
            else:
                return 2 if board[r2+2][c] > 0 else 1

def dfs(board:list, cards:list, order:tuple, idx:int, cnt:int, minCnt:list, r:int, c:int) -> None:
    if idx == len(order):
        minCnt[0] = min(minCnt[0], cnt)
        return

    card = order[idx]
    
    r1, c1 = cards[card][0][0], cards[card][0][1]
    r2, c2 = cards[card][1][0], cards[card][1][1]

    # 1번부터
    dis = get_distance(board, r, c, r1, c1)
    board[r1][c1] = 0
    dis += get_distance(board, r1, c1, r2, c2)
    board[r2][c2] = 0
    dfs(board, cards, order, idx+1, cnt + dis, minCnt, r2, c2)

    # 백트래킹
    board[r1][c1] = card
    board[r2][c2] = card

    # 2번부터
    dis = get_distance(board, r, c, r2, c2)
    board[r2][c2] = 0
    dis += get_distance(board, r2, c2, r1, c1)
    board[r1][c1] = 0
    dfs(board, cards, order, idx+1, cnt + dis, minCnt, r1, c1)

    board[r1][c1] = card
    board[r2][c2] = card

def solution(board:list, r:int, c:int):
    cards = [[] for i in range(7)]
    cardSet = set()
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                cards[board[i][j]].append((i, j))
                cardSet.add(board[i][j])
    
    answer = [73]
    P = list(permutations(list(cardSet), len(cardSet)))
    for p in P:
        dfs(board, cards, p, 0, 0, answer, r, c)
    
    return answer[0] + len(cardSet) * 2
