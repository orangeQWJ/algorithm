def func1(str):
    l = list(str)
    l.sort()
    return "".join(l)


def groupAnagrams(strs):
    # 为每一个字符穿打上标签
    strs = [(func1(s), s) for s in strs]
    strs.sort()
    d = {}
    for x in strs:
        if x[0] not in d:
            d[x[0]] = [x[1]]
        else:
            d[x[0]].append(x[1])
    re = []
    for _, v in d.items():
        re.append(v)
    return re


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
re = groupAnagrams(strs)
for x in re:
    print(x)

"""
改进
"""

def groupAnagrams2(strs):

    from collections import defaultdict
    mp = defaultdict(list)
    for st in strs:
        key = "".join(sorted(st))
        mp[key].append(st)
    return list(mp.values())


def groupAnagrams3(strs):
    # 字母异位词有一个共同分特征,每个字母出现相同次数
    # "ABCabc"
    from collections import defaultdict
    mp = defaultdict(list)
    for str in strs:
        count = [0] * 26
        for ch in str:
            count[ord(ch)-ord('a')] += 1
        mp[tuple(count)].append(str)
    return list(mp.values())

if __name__ == "__main__":
    print("..........")
    re = groupAnagrams2(strs)
    for x in re:
        print(x)

    print("..........")
    re = groupAnagrams3(strs)
    for x in re:
        print(x)

