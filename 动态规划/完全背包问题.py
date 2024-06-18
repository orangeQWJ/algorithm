coins = [5, 2, 1]
W = 6

L = len(coins)

# i max_value L-1
# j max_value W

dp = [[0] * (W+1) for _ in range(L)]

# base case

dp[0][0] = 0
# dp[0][...] 只使用第一种面值
for j in range(1, W+1):
    if j % coins[0] == 0:
        dp[0][j] = 1

# dp[...][0] 凑齐0
for i in range(1, L):
    dp[i][0] = 1


for x in dp:
    print(x)
print("=======")

for i in range(1, L):
    for j in range(1, W+1):
        if j >= coins[i]:
            dp[i][j] = dp[i][j-coins[i]] + dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]
for x in dp:
    print(x)
print(dp[L-1][W])
