n = 3
choice = ["("] * n + [")"] * n

reslut = set()


def l2s(l):
    return "".join(l)


def func(path, choice, R, L):
    if len(path) == n*2:
        reslut.add(l2s(path))
        return
    for i, c in enumerate(choice):
        if c == ')' and R == L:
            continue
        path.append(c)
        if c == '(':
            L += 1
        else:
            R += 1
        remain_choice = choice.copy()
        remain_choice.pop(i)
        func(path, remain_choice.copy(), R, L)
        path.pop()
        if c == '(':
            L -= 1
        else:
            R -= 1


func([], choice, 0, 0)
for x in reslut:
    print(x)
