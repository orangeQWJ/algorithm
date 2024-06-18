A = [0, 0, 0, 0]

def l2s(l):
    s = ""
    for x in l:
        s += str(x)
    return s

def s2l(s):
    l = []
    for x in s:
        l.append(int(x))
    return l

def lj(s):
    a = s2l(s)
    a_init = a.copy()
    ljNode = []
    for i in range(4):
        a[i] = (a_init[i]+1) % 10
        ljNode.append(l2s(a.copy()))
        a[i] = (a_init[i]+9) % 10
        ljNode.append(l2s(a.copy()))
        a[i] = a_init[i]
    return ljNode

visited = set()
deepth = 0
target = "8767"
#deadens = lj(target)
deadens = "8768"
start = "0000"
st = []

def bfs():
    global deepth
    st.append(start)
    while len(st) > 0:
        sz = len(st)
        print(sz)
        for _ in range(sz):
            cur = st.pop(0)
            if cur in deadens:
                continue
            if cur == target:
                print(deepth)
                return True
            cur_adjs = lj(cur)
            for j in cur_adjs:
                if j not in visited:
                    visited.add(j)
                    st.append(j)
        deepth += 1
    return False
print(bfs())



