def get_horizon_count(vertical: list, R: int, SUM: int) -> int:
    SUM -= vertical[0]
    if SUM == 0:
        return 0

    count = 0
    for i in range(1, R+1):
        SUM -= vertical[i]
        count += 1
        if SUM == 0:
            return count
    count += R
    for i in range(len(vertical)-1, -1, -1):
        SUM -= vertical[i]
        count += 1
        if SUM == 0:
            return count

def solution(name):
    vertical = [0 for _ in range(len(name))]
    # N까지는 위로 누르는 것이 최선
    for i in range(len(name)):
        ch = name[i]
        if ch <= 'N':
            vertical[i] = ord(ch) - ord('A')
        else:
            vertical[i] = 1 + ord('Z') - ord(ch)

    SUM = sum(vertical)
    horizon = len(name)
    for R in range(len(name)):
        horizon = min(horizon, get_horizon_count(vertical, R, SUM))

    return SUM + horizon
