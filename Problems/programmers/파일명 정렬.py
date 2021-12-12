from functools import cmp_to_key


def compare(filename1: str, filename2: str):
    head1 = filename1[0].upper()
    head2 = filename2[0].upper()

    if head1 == head2:
        number1, number2 = int(filename1[1]), int(filename2[1])
        return number1 - number2
    else:
        return -1 if (head1 <= head2) else 0


def solution(files):
    filenames = []
    for file in files:
        filenames.append(split_file_name(file))
    filenames.sort(key=cmp_to_key(compare))

    answer = []
    for filename in filenames:
        answer.append(filename[0] + str(filename[1]) + filename[2])
    return answer


def split_file_name(filename: str) -> list:  # 파일 이름을 [HEAD, NUMBER, TAIL]로 나눔
    for i, ch in enumerate(filename):
        if ch.isnumeric():
            for j in range(i + 1, len(filename)):
                if not filename[j].isnumeric():
                    return [filename[:i], filename[i:j], filename[j:]]
            return [filename[:i], filename[i:], '']
