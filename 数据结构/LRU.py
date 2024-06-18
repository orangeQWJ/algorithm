from collections import OrderedDict


class LRU:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return False, -1
        self.cache.move_to_end(key)
        return True, self.cache[key]

    def put(self, key, val):
        if key in self.cache:
            self.cache[key] = val
            self.cache.move_to_end(key)
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = val
            self.cache.move_to_end(key)

if __name__ == "__main__":
    cache = LRU(2)
    cache.put(1, 1)
    cache.put(2, 2)
    # [1:1 , 2:2]
    print(cache.get(1))
    # [2:2, 1:1]
    cache.put(3,3)
    # [2:2, 1:1, 3:3]
    # [1:1, 3:3]
    print(cache.get(2))
    cache.put(4,4)
    # [1:1, 3:3, 4:4]
    # [3:3, 4:4]
    print(cache.get(1))
