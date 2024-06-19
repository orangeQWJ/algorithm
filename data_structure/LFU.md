# LFU

当内存不够时，删除使用最近使用次数最少的额
缓存容量为 2，A 最近使用了 8 次，B 最近使用了 2 次。当 C 到来会删除 B

## LFU 算法描述

1. 初始化时接受参数 `capacity` 作为容量
2. `put(key, val)` 存入值, 时间复杂度 O(1)
3. `get(key)` 尝试获取值, 时间复杂度 O(1)

## 需求分析

1. 必须记住元素的时序, 挑选最久未使用元素
2. 必须快速找到某个 `key` 对应的 `value`
3. 每次访问(key/put)一个元素 `key` ,需要将这个元素的使用次数+1

## 实现思路

1. cache 是一个字典,存储每一个 key,以及他的值和访问次数

   ```python
   cache =  {
   		key1 :( val1, freq1)
   		key2 :( val2, freq2)
   	}
   ```

2. 当我们要删除一个元素时,需要知道最小的 frq. 然后根据 freq 找到对应的 key.
   每个 freq 可能对应多个 key. 先写出一个满足功能要求的结构
   ```python
   freqMap = {
      1 : [ key1, key2 ],
      2 : [ key3, key4 ],
      8 : [ key5, key6 ],
      100 : [ key7 ],
   }

   ```
   **缺陷**
   1. 无法快速删除当key被操作时,需要从一个freq列表转一个一个新的frq列表.
   2. 可以将列表换成集合
   
   ```Python
   freqMap = {
      1 : { key1, key2 },
      2 : { key3, key4 },
      8 : { key5, key6 },
      100 : { key7 },
   }
   ```

   ```

### min_freq 当需要删除一个元素时需要知道当前最小的访问次数是多少 
min_freq 的变化情况有两种
1. 新插入一个(key,value), min_freq = 1
2. 当一个 n : [] 变为空, 如果 min_freq == n  => min_freq = n + 1
