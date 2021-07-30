from collections import defaultdict

class MapSum:

    def __init__(self):
        self.repository = defaultdict(int)
        
    def insert(self, key: str, val: int) -> None:
        self.repository[key] = val      

    def sum(self, prefix: str) -> int:
        result = 0
        for key in self.repository.keys():
            if key.startswith(prefix):
                result += self.repository[key]
        return result
