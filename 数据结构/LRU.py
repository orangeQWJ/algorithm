from collections import OrderedDict 


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return False, -1
        self.cache.move_to_end(key) # 设定:排在最后面的被认为是最近被操作的
        return True, self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value # 新元素会放在队尾,所以我在设计时,认为排在最后面的是最今被操作的.
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    cache = LRUCache(2)
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
    # [3:3, 4:4]
