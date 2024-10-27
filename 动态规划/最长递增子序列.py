nums = [10, 9, 2, 5, 3, 7, 99, 18]

# dp[i] 以nums[i] 结尾的最长递增子序列长度

# 初始化 dp 数组，所有元素初始为 1
dp = [1 for _ in range(len(nums))]

# 计算 dp 数组
# dp[大] 依赖 dp[小]. i 从小到大
for i in range(1, len(nums)):
    for j in range(i):
        # 如果当前元素大于之前的元素
        if nums[i] > nums[j]:
            # 更新 dp[i] 为 dp[j] + 1 和 dp[i] 的最大值
            dp[i] = max(dp[j] + 1, dp[i])

# 验证结果
# 输出每个 dp 值
for i, v in enumerate(dp):
    print(i, v)
# 输出最长递增子序列的长度
print(max(dp))

# 备忘录
memo = {}
# base_case
memo[0] = 1

# func(i) 以nums[i] 结尾的最长递增子序列
def func(i):
    # 如果已经计算过，直接返回结果
    if i in memo:
        return memo[i]
    max_length = 1
    # 遍历之前的元素
    for j in range(i):
        # 如果当前元素大于之前的元素
        if nums[i] > nums[j]:
            # 递归计算并更新最大长度
            max_length = max(func(j) + 1, max_length)
    # 存储计算结果
    memo[i] = max_length
    return max_length

# 计算每个元素的最长递增子序列长度
for i in range(len(nums)):
    func(i)

# 输出备忘录中的结果
for k, v in memo.items():
    print(k, v)
# 输出最长递增子序列的长度
print(max(memo.values()))
