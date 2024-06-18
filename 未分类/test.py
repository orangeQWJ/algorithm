choice = [1,2,3]


result = []


def backtrace(path, choice):
    if len(path) == 3:
        result.append(path.copy())
        return
    for i, x in enumerate(choice):
        new_choiece = choice.copy()
        new_choiece.pop(i)
        path.append(x)
        backtrace(path, new_choiece)
        path.pop()

backtrace([], choice)

for x in result:
    print(x)
