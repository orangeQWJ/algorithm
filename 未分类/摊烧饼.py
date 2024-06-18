A = [3,2,4,1]

def func1(d):
    # 将[0:d] 的最大元素放在d上
    tempA = A[:d+1]
    i_max = A.index(max(tempA))
    if i_max == d:
        return
    A[:i_max+1] = A[:i_max+1][::-1]
    print(i_max+1)
    print(d+1)
    A[:d+1] = A[:d+1][::-1]



func1(3)
print(A)
func1(2)
print(A)
func1(1)
print(A)
