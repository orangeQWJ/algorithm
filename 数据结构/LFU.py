from collections import defaultdict


class LFU:
    def __init__(self, capacity):
        self.cache = dict()
        self.freqMap = defaultdict(set)
        self.capacity = capacity
        self.min_freq = 1

    def update_freq(self, key):
        val, freq = self.cache[key]
        self.freqMap[freq].remove(key)
        if len(self.freqMap[freq]) == 0:
            if self.min_freq == freq:
                self.min_freq += 1
            del self.freqMap[freq]
        self.freqMap[freq+1].add(key)
        self.cache[key] = (val, freq+1)

    def put(self, key, val):
        if key in self.cache:
            self.update_freq(key)
            _, new_freq = self.cache[key]
            self.cache[key] = val, new_freq
        else:
            if len(self.cache) == self.capacity:
                key_todel = self.freqMap[self.min_freq].pop()
                if len(self.freqMap[self.min_freq]) == 0:
                    del self.freqMap[self.min_freq]
                del self.cache[key_todel]

            self.cache[key] = (val, 1)
            self.freqMap[1].add(key)
            self.min_freq = 1

    def get(self, key):
        if key not in self.cache:
            return False, None
        self.update_freq(key)
        return True, self.cache[key][0]


if __name__ == "__main__":
    # import pudb
    # pudb.set_trace()
    #
    lfu = LFU(2)
    lfu.put(1, 1)
    lfu.get(1)  # 返回 1
    lfu.put(2, 2)
    lfu.put(3, 3)
    lfu.put(4, 4)
    lfu.get(4)
    lfu.get(4)
    print(lfu.cache)
    print(lfu.freqMap)
