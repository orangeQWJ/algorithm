nums = [3, 4, -6, 4, 5, -19, 5, 6, -3, 4]

# dp[i] = 以nums[i] 开头的最大子数组之和
dp = [0] * len(nums)
# 初始条件
dp[-1] = nums[-1]

# dp[小] 依赖dp[大],所以先计算dp[大]
for i in range(len(nums)-2, -1, -1):
    dp[i] = max(dp[i+1] + nums[i], nums[i])
print(max(dp))
