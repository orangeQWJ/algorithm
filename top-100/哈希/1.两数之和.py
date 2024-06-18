def twoSum(nums, target):
    # fast_find: 你要什么,我立马给你下标
    # fast_find[key] = value
    # nums 中的key 在下标value位置处
    fast_find = {}
    for i, x in enumerate(nums):
        # desiredElement
        dE = target - x
        if dE in fast_find:
            return [i, fast_find[dE]]
        else:
            fast_find[x] = i
    return []


r = twoSum([2, 7, 11, 15], 9)
print(r)
r = twoSum([3, 2, 4], 6)
print(r)
r = twoSum([3, 3], 6)
print(r)
