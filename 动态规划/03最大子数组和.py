nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# dp[i] 以nums[i] 开头的最大子数组

# base_case

dp = nums[:]

for i in range(len(nums)-2, -1, -1):
    dp[i] = max(dp[i+1] + nums[i], nums[i])

print(max(dp))
