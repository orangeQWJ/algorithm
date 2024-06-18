import math
import random
nums = [x for x in range(100) if x % 2 == 0]
# nums [0 2 4 .... 98]


def func1(nums, aim, down):
    L = 0
    R = len(nums) - 1

    mid = 0
    while L <= R:
        if down == True:
            mid = (L + R) // 2
        else:
            mid = math.ceil((L+R)/2)
        if nums[mid] == aim:
            print("命中 index:{0}".format(mid))
            break
        elif nums[mid] < aim:
            L = mid + 1
        else:
            R = mid - 1
    print("M:{0}".format(mid))
    if L == len(nums):
        print("L: 越界")
    else:
        print("L: [{0}]={1}".format(L, nums[L]))

    if R == -1:
        print("R: 越界")
    else:
        print("R: [{0}]={1} ".format(R, nums[R]))


# case 1
nums = [random.randint(1, 100) for _ in range(10000)]
nums.sort()
# func1(nums, -10, True)
# func1(nums, -10, False)
# case 2
nums = [x for x in range(100) if x % 10 == 0]
nums.sort()
# func1(nums, 9, True)
# func1(nums, 9, False)
# case 3
nums = [x for x in range(100) if x % 10 == 0]
nums.sort()
# func1(nums, 44, True)
# func1(nums, 44, False)
# case 4
nums = [x for x in range(100) if x % 10 == 0]
nums.sort()
# func1(nums, 88, True)
# func1(nums, 88, False)
# case 5
nums = [x for x in range(100) if x % 10 == 0]
nums.sort()
# func1(nums, 101, True)
# func1(nums, 101, False)


l = [
    (
     random.randint(0, 100), random.choice(
         ["one", "two", "three", "four", "five"])
     )
    for _ in range(999)
]


def mysort(x):
    trans = {
        "three": 5,
        "four": 4,
        "one": 3,
        "two": 2,
        "five": 1,
    }
    return (-1*x[0], trans[x[1]])


l.sort(key=mysort)
for x in l:
    print(x)


