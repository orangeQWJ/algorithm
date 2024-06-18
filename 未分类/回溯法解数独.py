n = 9
borad = [["."]*n for _ in range(n)]
borad[0][0] = 4


def isValid(i, j, x):
    for t in range(n):
        if borad[i][t] == x:
            return False
        if borad[t][j] == x:
            return False
        if borad[(i//3)*3 + t//3][(j//3)*3 + t % 3] == x:
            return False
    return True


reslut = []
end = False
def xq(i, j):
    global end
    if end:
        return
    if i == n:
        end = True
        for x in borad:
            print(x)
        return 
    if j == n:
        xq(i+1, 0)
        return
    if borad[i][j] != ".":
        xq(i, j+1)
        return
    for x in range(1, n+1):
        if not isValid(i, j, x):
            continue
        borad[i][j] = x
        print((i,j),"=",x)
        xq(i, j+1)
        borad[i][j] = '.'

xq(0,0)
