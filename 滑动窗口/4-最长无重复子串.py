s = "aababcabqc"

R = L = 0

window = {}
for x in s:
    window[x] = 0

max_length = 0
start = 0
while R < len(s):
    c = s[R]
    R += 1
    window[c] += 1

    while window[c] == 2:
        tmp_length = (R -1) -L
        if tmp_length > max_length:
            max_length = tmp_length
            start = L
        d = s[L]
        L += 1
        window[d] -= 1

print(s[start:start+max_length])
