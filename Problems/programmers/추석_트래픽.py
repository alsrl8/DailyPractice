def compareTime(time1, time2):
    for i in range(4):
        if(time1[i] < time2[i]):
            return 1
        elif(time1[i] > time2[i]):
            return 2
    if(time1[4] < time2[4] - 1):
        return 1
    elif(time1[4] - 1 > time2[4]):
        return 2
    return 0

def subTime(time):
    sub_ss = int(time[5])
    sub_ms = int((time[5] % 1) * 1000)
    sub_time = [0 for i in range(5)]
    sub_time[4] = time[4] - sub_ms
    if(sub_time[4] < 0):
        sub_time[4] += 1000
        sub_ss += 1
    sub_time[3] = time[3] - sub_ss - 1
    if(sub_time[3] < 0):
        sub_time[3] += 60
        sub_time[2] -= 1
    sub_time[2] += time[2]
    if(sub_time[2] < 0):
        sub_time[2] += 60
        sub_time[1] -= 1
    sub_time[1] += time[1]
    if(sub_time[1] < 0):
        sub_time[1] += 24
        sub_time[0] -= 1
    sub_time[0] += time[0]
    return sub_time

def solution(s):
    max = 0
    data = []
    for i in range(len(s)):
        time = []
        time.append(int(s[i][8:10]))
        time.append(int(s[i][11:13]))
        time.append(int(s[i][14:16]))
        time.append(int(s[i][17:19]))
        time.append(int(s[i][20:23]))
        time.append(float(s[i][24:len(s[i]) - 1]))
        data.append(time)
        
    for i in range(len(s)):
        cnt = 1
        for j in range(i + 1, len(s)):
            if(data[j][3] > data[i][3] + 4):
                break
            else:
                if(compareTime(data[i], subTime(data[j])) == 2):
                    cnt += 1
        if(max < cnt):
            max =cnt
    return max
