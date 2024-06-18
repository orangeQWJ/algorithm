# 子集
def func1(nums):
    if len(nums) == 0:
        return [[]]
    last_num = nums.pop()
    r = func1(nums.copy()) + [x + [last_num] for x in func1(nums.copy())]
    # r = func1(nums.copy()) + [x.append(last_num) for x in func1(nums.copy())]
    return r.copy()


#r = func1([1, 2, 3])

#print(len(r))

# 子集
reslut = []
def func2(path, choice):
    reslut.append(path.copy())
    for i, x in enumerate(choice):
        path.append(x)
        new_choice = choice.copy()
        new_choice.pop(i)
        func2(path, new_choice)
        path.pop()


#func2([], ["a","b","c"])

#for x in reslut:
    #print(x)

# 任2组合
reslut = []
def func3(path, choice):
    if len(path) == 2:
        reslut.append(path.copy())
        return 
    for i, x in enumerate(choice):
        if not path:
            path.append(x)
        elif x < path[-1]:
            continue
        else:
            path.append(x)
        new_choice = choice.copy()
        new_choice.pop(i)
        func3(path.copy(), new_choice)
        path.pop()

func3([], ["a","b","c"])
for x in reslut:
    print(x)
