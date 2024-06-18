# 自底向上--------------------------------------------------
nums = [10, 9, 2, 5, 3, 7, 101, 18]

# dp[i] = 以nums[i]这个数字结尾的最长递增子序列的长度
# 定义决定了数组的大小,和base case
dp = [1] * len(nums)

# dp[大] 依赖 dp[小]. i 从小到大
for i in range(1, len(nums)):
    for j in range(0, i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)
# 验证结果
for i, v in enumerate(dp):
    print(i, v)
print(max(dp))
# 自顶向下--------------------------------------------------
nums = [10, 9, 2, 5, 3, 7, 101, 18]
# 备忘录
memo = {0: 1}


def func(n):
    # 函数定义
    # func(i) 返回
    # 以nums[i]这个数字结尾的最长递增子序列的长度
    if n in memo.keys():
        return memo[n]
    # 查看调用次数,验证备忘录功效
    print("func(%d)" % n)

    max_length = 1
    # for i in range(0, n):
    for i in range(n-1, -1, -1):
        # i 从n-1到0
        if nums[n] > nums[i]:
            max_length = max(max_length, func(i)+1)

    memo[n] = max_length
    return memo[n]


# 更新备忘录
for i in range(len(nums)):
    func(i)
# 验证结果
for k, v in memo.items():
    print(k, v)
print(max(memo.values()))
