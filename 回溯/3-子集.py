choice = [1, 2, 3]

"""
[1]:
    [] [1]
[1,2]:
    [] [1]  +  [].append(2) [1].append(2)
"""


def Func(A):
    """
    返回A的子集
    返回值类型是以列表为元素的列表
    eg: [ [], [1] ]
    """
    # base_case:
    if not A:
        return [[]]
    else:
        last_element = A.pop()
        r = Func(A)
        # 常犯错误 list.append() 的返回值是None
        # return r + [x.append(last_element) for x in r]
        return r + [x + [last_element] for x in r]





r = Func(choice)

for x in r:
    print(x)
