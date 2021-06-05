import sys
from bisect import bisect_right

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

def cal(h:int) -> int:
    global trees
    start = bisect_right(trees, h)
    sum = 0
    for i in range(start, len(trees)):
        sum += (trees[i] - h)
    return sum

def binarySearch(left:int, right:int):
    global M
    middle = (left + right) // 2
    if left == middle:
        temp_left = cal(left)
        temp_right = cal(right)
        if temp_left == M:
            return left
        elif temp_right == M:
            return right
        else:
            return left

    result = cal(middle)
    if result == M:
        return middle
    elif result < M:
        return binarySearch(left, middle)
    else:
        return binarySearch(middle, right)

left = 0
right = trees[len(trees) - 1]
result = binarySearch(left, right)
print(result)
