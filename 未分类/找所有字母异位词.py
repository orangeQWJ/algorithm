def func():
    S = "cbaebabacd"
    T = "abc"
    
    L = R = 0
    valid = 0

    need = {}
    window = {}

    for x in T:
        if x not in need:
            need[x] = 1
        else:
            need[x] += 1

    for x in T:
        window[x] = 0


    while R < len(S):
        c = S[R]
        R += 1
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        while R - L >= len(T):
            if valid == len(T):
                print(L)
            d = S[L]
            L += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

func()
