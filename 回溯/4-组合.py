A = [1, 2, 3, 4, 5]

K = 4

# 从A中挑选K个

result = []


def Func(path, choice):
    if len(path) == K:
        result.append(path.copy())
        return
    for i, c in enumerate(choice):
        if path and c <= path[-1]:
            continue
        remain_choice = choice.copy()
        remain_choice.pop(i)
        path.append(c)
        Func(path, remain_choice)
        path.pop()


Func([], A)

for x in result:
    print(x)
