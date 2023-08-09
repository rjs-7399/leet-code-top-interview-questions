class LRUCache:
    def __init__(self, max_size=2):
        self.LRU = {}
        self.max_size = max_size

    def put(self, key, val):
        if key in self.LRU:
            del self.LRU[key]
            self.LRU[key] = val
        elif len(self.LRU) < self.max_size:
            self.LRU[key] = val
        else:
            first_index = next(iter(self.LRU))
            del self.LRU[first_index]
            self.LRU[key] = val

    def get(self, key):
        if key in self.LRU:
            temp_val = self.LRU[key]
            del self.LRU[key]
            self.LRU[key] = temp_val
            return self.LRU[key]
        else:
            return -1

if __name__ == "__main__":
    LRU_cache = LRUCache(max_size=2)
    print(LRU_cache.get(2))
    LRU_cache.put(2,6)
    print(LRU_cache.LRU)
    print(LRU_cache.get(1))
    LRU_cache.put(1,5)
    print(LRU_cache.LRU)
    LRU_cache.put(1,2)
    print(LRU_cache.LRU)
    print(LRU_cache.get(1))
    print(LRU_cache.get(2))