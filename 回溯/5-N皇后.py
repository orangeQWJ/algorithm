import copy
"""
N * N 棋盘上,放N个皇后.
每一行,每一列,每一斜线
只能有一个皇后

tip: 不是所有N能都成立
"""

N = 4
chessboard = [[0] * N for _ in range(N)]

"""
每次在一行上选一个位置
每一列只能被选一次,所以choice中可以放能被选择的列
行应该随着递归深度增加
放之前判断一下能不能放
套路中记录状态的path可以省略了,因为当前状态可以记录在chessboard中,撤销也在chessboard中完成 
"""


def isValid(i, j):
    """
    在i,j位置防止皇后是否合法
    """
    init_i = i
    init_j = j 
    # 列和行一定是合法的
    # 只需要检查,左上方,右上方是否有皇后

    # 左上方
    while i >= 0 and j >= 0:
        if chessboard[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # 右上方
    i = init_i
    j = init_j
    while i >= 0 and j <= N-1:
        if chessboard[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True


choice_col = list(range(N))

result = []
def Func(row, choice):
    if row == N:
        result.append(copy.deepcopy(chessboard))
        return
    for i, c in enumerate(choice):
        if not isValid(row, c):
            continue
        remain_choice = choice.copy()
        remain_choice.pop(i)
        chessboard[row][c] = 1
        Func(row+1, remain_choice)
        chessboard[row][c] = 0
Func(0, choice_col)

for x in result:
    for row in x:
        for col in row:
            print(col, end = " ")
        print()
    print("=========")
