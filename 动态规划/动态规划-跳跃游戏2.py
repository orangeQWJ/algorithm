nums = [2, 3, 1, 1, 4]

Max_distance = len(nums) + 100
# dp[i] 从下标i,跳到最后一个格子,最少需要的跳跃次数.

"""
nums[i] = 3
dp[i] = min(
        dp[i+1],
        dp[i+2],
        dp[i+3],
        ) + 1
从当前位置,只能跳到这三个位置,从这三个位置中选出一个后续最小的.

dp[小] 依赖 dp[大]
"""

# base case

dp = [Max_distance for _ in nums]

Len = len(nums)
for i in range(Len):
    distance = Len - 1 - i
    if nums[i] >= distance:
        dp[i] = 1

dp[-1] = 0
print("nums:")
print(nums)
print("inital dp:")
print(dp)

# 求dp[i]的值


def func(i):
    if nums[i] == 0:
        return i
    # 当前位置所能跳到的最远位置
    farthest = i + nums[i]
    # 不能超出最后一个元素
    farthest = min(len(nums)-1, farthest)
    min_value = dp[i]
    for index in range(i+1, farthest+1):
        print(index)
        if dp[index] + 1 < min_value:
            min_value = dp[index] + 1
    dp[i] = min_value


for i in range(len(nums)-2, -1, -1):
    func(i)
print("final dp:")
print(dp)
