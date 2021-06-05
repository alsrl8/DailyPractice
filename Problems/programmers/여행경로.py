def solution(tickets):
    dic = dict()
    for i in range(len(tickets)):
        if not dic.__contains__(tickets[i][0]):
            dic.update({tickets[i][0] : []})
        dic[tickets[i][0]].append(tickets[i][1])
    
    def dfs(st:str, answer:list):
        if len(answer) == len(tickets) + 1:
            return

        if not dic.__contains__(st):
            return
        dic[st].sort()
        for i in range(len(dic[st])):
            answer.append(dic[st][i])
            temp = dic[st][i]
            del dic[st][i]
            dfs(temp, answer)
            if len(answer) == len(tickets) + 1:
                return answer
            del answer[len(answer) - 1]
            dic[st].insert(i, temp)
    return dfs("ICN", ["ICN"])
