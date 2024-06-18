import copy
N = 9
"""
每行每列只能不能重复出现数字
9个3*3的格子里不能重复出现数字
已经下过的点不能下

tips: 某些位置上已经填好数
"""
B = [[-1] * N for _ in range(N)]

B[3][3] = 4
B[5][4] = 5


# 想要放弃选择,必须通过递归,在递归返回时撤销选择
# 在(i,j)处下棋这个动作想要撤销,必然要放到一个函数中递归调用

result = []


def isValid(i, j, x):
    for t in range(N):
        if B[i][t] == x:
            return False
        if B[t][j] == x:
            return False
        if B[(i//3)*3 + t//3][(j//3)*3 + t % 3] == x:
            return False
    return True


end = False



def Func(i, j):
    """
    尝试在(i,j) 处落子
    """
    global end
    if end:
        return
    # 使坐标合法化,之后再进行逻辑判断
    if j == N:
        i += 1
        j = 0
    # 结束
    if i == N:
        end = True
        result.append(copy.deepcopy(B))
        return
    # 下一步
    if B[i][j] != -1:
        Func(i, j+1)
        return
    for c in range(1, N+1):
        # 选择
        if isValid(i, j, c):
            B[i][j] = c
        else:
            continue
        Func(i, j+1)
        # 撤销选择
        B[i][j] = -1


Func(0, 0)

for x in result:
    for row in x:
        for col in row:
            print(col, end=" ")
        print()
