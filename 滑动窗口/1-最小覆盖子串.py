# 在s中找出包含t所有字母的全部最短子串

s = "ADBECFEBANC"
t = "ABC"

L = R = 0

valid = 0
min_length = len(s) * 2
start = 0

# 窗口需要满足的条件
need = {}
for x in t:
    need[x] = 1

# 窗口关心的状态
window = {}
for k in need:
    window[k] = 0

# 当前窗口 [L:R)
while R < len(s):
    c = s[R]
    R += 1
    if c in need:
        window[c] += 1
        if window[c] == need[c]:
            valid += 1
    while valid == len(need):
        tmp_length = R-L
        if tmp_length < min_length:
            start = L
            min_length = tmp_length
        d = s[L]
        L += 1
        if d in need:
            if window[d] == need[d]:
                valid -= 1
            window[d] -= 1


if min_length == len(s) * 2:
    print("")
else:
    print(s[start:start+min_length])
