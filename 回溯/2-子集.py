choice = [1, 2, 3]
result_set = set()

def Func(path, choice):
    result_set.add(tuple(path))
    for i, c in enumerate(choice):
        remain_choice = choice.copy()
        remain_choice.pop(i)
        path.append(c)
        Func(path, remain_choice)
        path.pop()


Func([], choice)

for x in result_set:
    print(x)

"""
时间复杂度高
[2, 3] , [3, 2] 都添加过一次.
通过集合特性过滤掉了
"""
choice = [1, 2, 3]
result_list = []
count = 0


def Func2(path, choice):
    global count
    result_list.append(path.copy())
    count += 1
    for i, c in enumerate(choice):
        remain_choice = choice.copy()
        remain_choice.pop(i)
        path.append(c)
        Func2(path, remain_choice)
        path.pop()


Func2([], choice)

print("exe add count:", count)
for x in result_list:
    print(x)

"""
往path中追加元素时,添加限制,不是什么样的都可以添加的
只能添加更大的元素,就可以避免添加[3,2] [3,1]等情况
"""


choice = [1, 2, 3]
result_list = []
count = 0



def Func3(path, choice):
    global count
    result_list.append(path.copy())
    count += 1
    for i, c in enumerate(choice):
        if path and c <= path[-1]:
            continue
        remain_choice = choice.copy()
        remain_choice.pop(i)
        path.append(c)
        Func3(path, remain_choice)
        path.pop()


Func3([], choice)

print("exe add count:", count)
for x in result_list:
    print(x)
