'''
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
'''


import pudb

def two_sum1(nums, target):
    """
    返回nums中一组和为target的两个数
    """
    nums.sort()
    L = 0
    R = len(nums) - 1
    while L < R:
        sum = nums[L] + nums[R]
        if sum < target:
            L += 1
        elif sum > target:
            R -= 1
        else:
            return [nums[L], nums[R]]
    return []


'''
print("=================================")
r = two_sum1([1, 2, 4, 5, 7, 8, 9], 16)
print()
'''


def two_sum2(nums, target):
    """
    返回nums中和为target的两个数
    不能出现重复
    """
    res = []
    nums.sort()
    L = 0
    R = len(nums) - 1
    while L < R:
        sum = nums[L] + nums[R]
        if sum < target:
            L += 1
        elif sum > target:
            R -= 1
        else:
            res.append([nums[L], nums[R]])
            L += 1
            R -= 1
    return res


'''
print("=================================")
nums = [1, 3, 1, 2, 2, 2, 2, 3, 3, 3]
print(sorted(nums))
# [1, 1, 2, 2, 2, 2, 3, 3, 3, 3]

r = two_sum2([1, 3, 1, 2, 2, 2, 2, 3, 3, 3], 4)
for x in r:
    print(x)
'''


def two_sum3(nums, target):
    """
    返回nums中和为target的两个数
    不能出现重复
    """
    res = []
    nums.sort()
    L = 0
    R = len(nums) - 1
    while L < R:
        sum = nums[L] + nums[R]
        if sum < target:
            L += 1
        elif sum > target:
            R -= 1
        else:
            res.append([nums[L], nums[R]])
            L_val = nums[L]
            R_val = nums[R]
            while L < R and nums[L] == L_val:
                L += 1
            while L < R and nums[R] == R_val:
                R -= 1
    return res


"""
print("=================================")
nums = [1, 3, 1, 2, 2, 2, 2, 3, 3, 3]
r = two_sum3(nums, 4)
for x in r:
    print(x)
"""


def threeSum(nums, target):
    """
    返回一个列表,列表每个元素是一个列表
    这个列表中的元素和为target==0
    nums = [-1, 0, 1, 2, -1, 4]
    [ 
        [-1, -1, 2],
        [-1, 0, 1],
    ]
    """
    res = []
    nums.sort()
    i = 0
    while i < len(nums):
        tar = target - nums[i]
        r = two_sum3(nums[i+1:], tar)
        for x in r:
            x.append(nums[i])
            res.append(x)
        val = nums[i]
        while i < len(nums) and nums[i] == val:
            i += 1
    return res


'''
print("=================================")
nums = [-1, 0, 1, 2, -1, 4]
# [1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
r = threeSum(nums, 0)
for x in r:
    print(x)
'''
nums = [1, 0, -1, 0, -2, 2]
target = 0


def nSum(n, nums, target):
    if n < 2 or not nums:
        return []
    elif n == 2:
        res = []
        L = 0
        R = len(nums) - 1
        while L < R:
            sum = nums[L] + nums[R]
            if sum < target:
                L += 1
            elif sum > target:
                R -= 1
            else:
                L_val = nums[L]
                R_val = nums[R]
                res.append([L_val, R_val])
                while L < R and nums[L] == L_val:
                    L += 1
                while L < R and nums[R] == R_val:
                    R -= 1
        return res
    i = 0
    res = []
    while i < len(nums):
        tar = target - nums[i]
        r = nSum(n-1, nums[i+1:], tar)
        for x in r:
            x.append(nums[i])
            res.append(x)
        val = nums[i]
        while i < len(nums) and nums[i] == val:
            i += 1
    return res


#pudb.set_trace()
nums.sort()

r = nSum(6, nums, 0)
for x in r:
    print(x)
