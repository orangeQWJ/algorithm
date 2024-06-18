"""
N 对 (), 给出所有的合法括号

思路:剪枝全排列
"""
N = 3

choice = ['('] * N + [')'] * N

result = set()
L_num = 0
R_num = 0
def Func(path, choice):
    global L_num, R_num
    if len(path) == N * 2:
        result.add(''.join(path))
        return
    for i, c in enumerate(choice):
        if L_num == R_num and c == ')':
            continue
        if c == '(':
            L_num += 1
        else:
            R_num += 1
        remain_choice = choice.copy()
        remain_choice.pop(i)
        path.append(c)
        Func(path, remain_choice)
        path.pop()
        if c == '(':
            L_num -= 1
        else:
            R_num -= 1


Func([], choice)

for x in result:
    print(x)
