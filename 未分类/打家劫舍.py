nums = [2, 7, 9, 3, 1]
nums = [1, 2]

L = len(nums)
# dp[i] 对[0:i]打家劫舍
# i max_value L - 1

dp = [0] * L

dp[0] = nums[0]

"""
dp[i] = max(
        nums[i] + dp[i-2],
        dp[i-1]
        )
"""

for i in range(1, L):
    if i-2 >= 0:
        dp[i] = max(
                nums[i] + dp[i-2],
                dp[i-1]
                )
    else:
        dp[i] = max(
                nums[i],
                dp[i-1]
                )

print(dp[L-1])

