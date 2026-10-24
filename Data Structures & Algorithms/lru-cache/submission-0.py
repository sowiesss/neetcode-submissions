class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.timer = 0
        self.cache = {}
        

    def get(self, key: int) -> int:
        v = self.cache.get(key)
        if not v:
            return -1
        else:
            self.cache[key] = (self.timer, v[1])
            self.timer += 1
            return v[1]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and self.capacity <= 0:
            items = sorted(self.cache.items(), key=lambda x: x[1])
            k, v = items[0]
            del self.cache[k]

        elif key not in self.cache:
            self.capacity -= 1
            
        self.cache[key] = (self.timer, value)
        self.timer += 1
        
