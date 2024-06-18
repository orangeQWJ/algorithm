# 信封
nums = [
    [5, 4],
    [5, 2],
    [6, 4],
    [6, 7],
    [1, 8],
    [2, 3],
]


def mysort(x):
    """
    第一元素升序,
    第二元素降序
    """
    return (x[0], -1 * x[1])


def func1(nums):
    """
    第一元素升序,
    第二元素降序
    """
    nums.sort(key=mysort)

    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i][1] > nums[j][1]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)


print(func1(nums))


def func2(nums):
    """
    第一元素升序
    第二元素升序
    """
    nums.sort()
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(0, i):
            # 额外的检查避免漏洞
            if nums[i][1] > nums[j][1] and nums[i][0] > nums[j][0]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)


print(func2(nums))
