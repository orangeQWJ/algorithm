import copy
N = 6
chessboard = [[0] * N for _ in range(N)]
# 每一行列只能选一次
choice = list(range(N))

reslut = []


def check(i, j):
    i_init = i
    j_init = j
    # 检查左上角
    while True:
        if not (i - 1 >= 0 and j - 1 >= 0):
            # 检查到头了
            break
        i -= 1
        j -= 1
        if chessboard[i][j] == 1:
            return False
    i = i_init
    j = j_init
    # 检查右上角
    while True:
        if not (i-1 >= 0 and j + 1 <= N-1):
            break
        i -= 1
        j += 1
        if chessboard[i][j] == 1:
            return False
    return True

def backtrack(level, choice):
    if level == N :
        reslut.append(copy.deepcopy(chessboard))
        return
    for i, j in enumerate(choice):
        chessboard[level][j] = 1
        if not check(level, j):
            chessboard[level][j] = 0
            continue
        remain_choice = choice.copy()
        remain_choice.pop(i)
        backtrack(level+1, remain_choice)
        chessboard[level][j] = 0

backtrack(0, choice)

for x in reslut:
    for j in x:
        print(j)
    print("======")
