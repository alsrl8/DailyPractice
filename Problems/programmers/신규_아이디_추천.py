def solution(new_id:str):
    new_id = new_id.lower()
    temp = ""
    arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-','_','.','1','2','3','4','5','6','7','8','9','0']
    for i in range(len(new_id)):
        if not new_id[i] in arr:
            continue
        temp += new_id[i]
    new_id = temp
    while new_id.find('..') >= 0:
        new_id = new_id.replace('..', '.')
    if new_id != '' and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id != '' and new_id[-1] == '.':
        new_id = new_id[:-1]
    if new_id == '':
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    while len(new_id) <= 2:
        last = new_id[-1]
        new_id += last
    return new_id
