s = "cbaebabacd"
t = "abc"

L = R = 0
valid = 0

result = []
need = {}
for x in t:
    if t in need:
        need[x] += 1
    else:
        need[x] = 1

window = {}
for k in need:
    window[k] = 0

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
            result.append(L)
        d = s[L]
        L += 1
        if d in need:
            if window[d] == need[d]:
                valid -= 1
            window[d] -= 1

for x in result:
    print(x, s[x:x+len(t)])
