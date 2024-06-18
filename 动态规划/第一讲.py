def fib2(n):
    # 确定dp[i]的含义
    # dp[i] = fib(i)
    # dp数组规模
    dp = [0] * (n + 1)
    # base_case
    dp[0] = 0
    dp[1] = 1
    # dp 数组遍历方向
    # fib(i) = fib(i-1) + fib(i-2)
    # dp[i] = dp[i-1] + dp[i-2]
    # dp[大] 依赖 dp[小]  所以先算dp[小]
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def fib3(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    # prev初始为dp[1]
    prev = 1
    # curr初始为dp[2]
    curr = 1
    # 注意迭代次数
    # 注意i = 3时，迭代了1轮，迭代结束 curr == dp[3]
    # 注意i = 4时，迭代了2轮，迭代结束 curr == dp[4]
    # 所以 i = n 时，迭代结束时 curr == dp[n]
    # range 前闭后开 so ...
    for i in range(3, n + 1):
        sum = prev + curr
        prev = curr
        curr = sum
    return curr



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
