from collections import OrderedDict, defaultdict


class LFUCache:
    def __init__(self, cap):
        self.cap = cap
        self.size = 0
        self.cache = {} # 主存储, key:(value,freq)
        self.freq_map = defaultdict(OrderedDict) # 频率映射, freq-> OrderedDict(key->value)
        self.min_freq = 1

    def _update_freq(self, key):
        value, freq = self.cache[key]
        # 从当前频率的 OrderedDict中删除key
        del self.freq_map[freq][key]
        if len(self.freq_map[freq]) == 0:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        new_frq = freq + 1
        self.freq_map[new_frq][key] = value
        self.cache[key] = (value, new_frq)

    def get(self, key):
        if key not in self.cache:
            return False, -1
        self._update_freq(key)
        return True, self.cache[key][0]

    def put(self, key, value):
        if key in self.cache:
            freq = self.cache[key][1]
            self.cache[key] = (value, freq)
            self.freq_map[freq][key] = value
            self._update_freq(key)
        else: # 不在队列中
            if self.size == self.cap: # 满了,先删除
                key_todel, _ = self.freq_map[self.min_freq].popitem(last=False)
                del self.cache[key_todel]
                self.size -= 1
            self.cache[key] = value, 1
            self.freq_map[1][key] = value
            self.min_freq = 1
            self.size += 1

if __name__ == "__main__":
    #import pudb
    #pudb.set_trace()
    #
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    print(lfu.get(1)[1])  # 返回 1
    lfu.put(3, 3)      # 该操作会使得 key 2 作废
    print(lfu.get(2)[1])  # 返回 -1 (未找到)
    print(lfu.get(3)[1])  # 返回 3
    lfu.put(4, 4)      # 该操作会使得 key 1 作废
    print(lfu.get(1)[1])  # 返回 -1 (未找到)
    print(lfu.get(3)[1])  # 返回 3
    print(lfu.get(4)[1])  # 返回 4
