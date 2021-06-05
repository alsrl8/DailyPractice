def solution(s):
    ll = len(s)
    answer = ll
    for l_substr in range(1, ll // 2 + 1):
        substr = s[0:l_substr]
        cnt = 1
        result = ""
        for i in range(1, ll // l_substr + 1):
            if(substr == s[i * l_substr : (i+1) * l_substr]):
                cnt += 1
            else:
                if(cnt > 1):
                    result += str(cnt)
                    cnt = 1
                result += substr
                substr = s[i * l_substr : (i+1) * l_substr]
        if(ll % l_substr > 0):
            result += s[l_substr * (ll // l_substr) : ll]
        #print("result = " + str(result))
        if(len(result) < answer):
            answer = len(result)
    return answer
