class LRUCache:
    def __init__(self, capacity: int):
        self.capa = capacity
        self.memory = {}

    def get(self, key: int) -> int:
        if key in self.memory:
            val = self.memory[key]
            del self.memory[key]
            self.memory[key] = val
            return self.memory[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.memory) == self.capa:
            if key in self.memory:
                del self.memory[key]
                self.memory[key] = value
            else:
                for k in self.memory:
                    del_k = k
                    break
                del self.memory[del_k]
                self.memory[key] = value
        else:
            if key in self.memory:
                del self.memory[key]
            self.memory[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
