"""
result = []
def backtrack(路径,选择列表):
    if 满足条件:
        reslut.add(路径)
        return
    for 选择 in 选择列表:
        做选择
            if 不满足:
                撤销选择
                contine
        backtrack(路径, 剩余选择列表)
        撤销选择

在for循环中做递归
在递归之前做选择
在递归之后撤销选择
"""

nums = [1, 2, 3]

result = []


def backtrack(path, choice):
    if len(path) == len(nums):
        result.append(path.copy())
        return
    for i, step in enumerate(choice):
        path.append(step)
        new_choice = choice.copy()
        new_choice.pop(i)
        backtrack(path, new_choice)
        path.pop()


backtrack([], [1, 2, 3])
print(len(result))
