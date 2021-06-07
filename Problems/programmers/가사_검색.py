class Trie:
    ahead = dict()
    behind = dict()

    def add(self, s:str):
        cur = self.behind
        for i in range(len(s)):
            ch = s[i]
            LEN = len(s) - i
            if not cur.__contains__(ch):
                cur.update({ch:dict()})
            if not cur.__contains__(LEN):
                cur.update({LEN:0})
            cur[LEN] += 1
            cur = cur[ch]
        
        cur = self.ahead
        for i in range(len(s)-1, -1, -1):
            ch = s[i]
            LEN = i + 1
            if not cur.__contains__(ch):
                cur.update({ch:dict()})
            if not cur.__contains__(LEN):
                cur.update({LEN:0})
            cur[LEN] += 1
            cur = cur[ch]

    def search(self, query:str) -> int:
        if query[0] == '?':
            cur = self.ahead
            idx = query.rfind('?')
            cnt = idx + 1
            for i in range(len(query)-1, -1, -1):
                ch = query[i]
                if ch == '?':
                    break
                elif not cur.__contains__(ch):
                    return 0
                cur = cur[ch]
            return cur[cnt] if cur.__contains__(cnt) else 0
        else:
            cur = self.behind
            idx = query.find('?')
            cnt = len(query) - idx
            for i in range(idx):
                ch = query[i]
                if not cur.__contains__(ch):
                    return 0
                cur = cur[ch]
            return cur[cnt] if cur.__contains__(cnt) else 0            

def solution(words, queries):
    answer = []
    trie = Trie()
    
    for word in words:
        trie.add(word)

    for query in queries:
        answer.append(trie.search(query))

    return answer