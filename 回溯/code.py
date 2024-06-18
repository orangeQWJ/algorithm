choice = [1, 2, 3]
result = []


def backtrace(path, choice):
    # 判断当前path是否满足条件
    if len(path) == 3:
        result.append(path.copy)
    # 做选择
    for i, c in enumerate(choice):
        remain_choice = choice.copy()
        remain_choice.pop(i)
        # 做出选择
        path.append(c)
        backtrace(path, remain_choice)
        # 撤销选择
        path.pop(c)
