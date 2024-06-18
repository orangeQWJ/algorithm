"""
4 位拨轮密码锁,0-9
每一次拨动有两个方向,0->1 0->9

从初始状态,最少拨几次,才能拨到目标状态期?
中间不能经过deadends["xxxx", "1234", ....]
"""
init = "0000"
target = "8767"
deadends = ["8768"]
visited = set()

def s2l(s):
    return [int(x) for x in s]
def l2s(l):
    l = [str(x) for x in l]
    return "".join(l)

def f_nb(s):
    l = s2l(s)
    result = []
    for i, x in enumerate(l):
        l[i] = (x + 1 ) % 10
        result.append(l2s(l))
        l[i] = (x + 9) % 10
        result.append(l2s(l))
        l[i] = x
    return result



Q = []
visited = set()
def bfs_bad():
    Q.append(init)
    deep = 0
    while len(Q) > 0:
        size = len(Q)
        print(size)
        for _ in range(size):
            cur = Q.pop(0)
            if cur in visited:
                print("重复访问", cur)
            visited.add(cur)
            if cur == target:
                print(deep)
                return True
            cur_nb = f_nb(cur)
            for j in cur_nb:
                if j not in visited:
                    Q.append(j)
        deep += 1
    return False

#      1
#     / \
#    2   3
#   / \ / \ 
#  4   5   6
"""
bfs_bad 在访问时才标记为被访问.
5 节点,再被访问之前先后被2,3加入到队列中
为了避免一个节点被重复加到队列中,当队列中加入节点后, 应该理解标记为added

在bfs中先添加到队列中意味着先被访问.
"""

Q = []
Added = set()
for x in deadends:
    Added.add(x)

def bfs_good():
    Q.append(init)
    Added.add(init)
    deep = 0
    while len(Q) > 0:
        size = len(Q)
        for _ in range(size):
            cur = Q.pop(0)
            if cur == target:
                print(deep)
                return
            cur_nb = f_nb(cur)
            for j in cur_nb:
                if j not in Added:
                    Added.add(j)
                    Q.append(j)
        deep += 1
    print(False)
bfs_good()
