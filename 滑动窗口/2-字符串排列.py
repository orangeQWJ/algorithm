# s 中是否包含 t 的全排列
s = "helloworld"
t = "oow"


L = R = 1
valid = 0

need = {}
for x in t:
    if x in need:
        need[x] += 1
    else:
        need[x] = 1
window = {}
for k in need:
    window[k] = 0

Flag = False

while R < len(s):
    c = s[R]
    R += 1
    if c in need:
        window[c] += 1
        if window[c] == need[c]:
            valid += 1
    while valid == len(need):
        tmp_length = R - L
        if tmp_length == len(t):
            Flag = True
            print(s[L:R])
        d = s[L]
        L += 1
        if d in need:
            if window[d] == need[d]:
                valid -= 1
            window[d] -= 1
