def longestConsecutive(nums):
    nums_set = set(nums)
    max_length = 1
    for n in nums:
        if n-1 not in nums_set:  # 说明n是一个开头元素
            start = n
            length = 1
            while start + 1 in nums_set:
                start += 1
                length += 1
            max_length = max(max_length, length)
    return max_length


re = longestConsecutive([100, 4, 200, 1, 3, 2])
print(re)
re = longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
print(re)


"""
变量名优化,提高可读性
"""


def longestConsecutive1(nums):
    max_len = 0
    nums_set = set(nums)

    for num in nums_set:
        if num - 1 not in nums_set:
            cur_num = num
            cur_len = 1
            while cur_num + 1 in nums_set:
                cur_num += 1
                cur_len += 1
            max_len = max(max_len, cur_len)
    return max_len


re = longestConsecutive1([100, 4, 200, 1, 3, 2])
print(re)
re = longestConsecutive1([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
print(re)
