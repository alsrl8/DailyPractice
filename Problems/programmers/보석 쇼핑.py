from collections import defaultdict
import heapq

def solution(gems):
    gems_dict = defaultdict(list)
    for i, gem in enumerate(gems):
        hq = gems_dict[gem]
        heapq.heappush(hq, i)

    gems_hq = []
    right_end = 0
    for gem in gems_dict.keys():
        heapq.heappush(gems_hq, (gems_dict[gem][0], gem))
        right_end = max(right_end, gems_dict[gem][0])

    answer = [gems_hq[0][0], right_end]

    while True:
        left_end, gem = heapq.heappop(gems_hq)
        heapq.heappop(gems_dict[gem])
        if len(gems_dict[gem]) == 0:
            break
        right_end = max(right_end, gems_dict[gem][0])
        heapq.heappush(gems_hq, (gems_dict[gem][0], gem))
        
        if answer[1]-answer[0] > right_end-gems_hq[0][0]:
            answer = [gems_hq[0][0], right_end]
    
    answer[0] += 1
    answer[1] += 1
    return answer
