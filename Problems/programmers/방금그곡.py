def solution(m, musicinfos):
    temp = []
    i = 0
    while i < len(m):
        if i + 1 < len(m) and m[i+1] == '#':
            temp.append(m[i] + '#')
            i += 2
        else:
            temp.append(m[i])
            i += 1
    m = temp

    playinfos = []
    for musicinfo in musicinfos:
        add_music(playinfos, musicinfo)

    playinfos.sort(key=lambda x: x[2], reverse=True)  # 재생 시간이 긴 순서대로 정렬

    for playinfo in playinfos:  # 음악 개수 <= 100
        music = playinfo[1]
        if is_match(music, m):
            return playinfo[0]

    return '(None)'


def add_music(playinfos: list, musicinfo: str):
    start, end, name, music = musicinfo.split(',')
    time = convert_HHMM_to_minutes(end) - convert_HHMM_to_minutes(start)

    melody = []
    idx_music = 0
    while len(melody) < time:
        ch = music[idx_music]
        if idx_music + 1 < len(music) and music[idx_music + 1] == '#':
            melody.append(ch + '#')
            idx_music += 2
        else:
            melody.append(ch)
            idx_music += 1

        if idx_music == len(music):
            idx_music = 0

    playinfos.append([name, melody, time])


def convert_HHMM_to_minutes(HHMM: str) -> int:
    HH, MM = HHMM.split(':')
    return int(HH) * 60 + int(MM)


def is_match(m1: list, m2: list) -> bool:  # len(m1) >= len(m2)
    i1 = 0
    end = len(m1) - len(m2) + 1
    while i1 < end:
        if m1[i1] == m2[0]:
            flag = True
            for i in range(len(m2)):
                if m1[i1+i] != m2[i]:
                    flag = False
                    break
            if flag:
                return True
        i1 += 1

    return False
