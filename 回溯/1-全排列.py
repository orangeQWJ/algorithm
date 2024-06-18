choice = [1, 2, 3]
result = []

def backtrace(path, choice):
    # 满足条件,保存. 一定要用copy()
    if len(path) == 3:
        result.append(path.copy())
        return
    for i, c in enumerate(choice):
        # 不能改变choice
        remain_choice = choice.copy()
        remain_choice.pop(i)
        # 做选择
        path.append(c)
        backtrace(path, remain_choice)
        # 撤销选择,在下一轮for中选择中换一新的.
        path.pop()


import pudb
pudb.set_trace()
backtrace([], choice)
for x in result:
    print(x)
