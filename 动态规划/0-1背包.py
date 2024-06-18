W = 7
N = 4
w = [1, 3, 4, 5]
v = [1, 4, 5, 7]

W = 10
w = [2,2,3,5]
v = [3,7,4,6]

dp = [[0]*(W+1) for _ in range(N)]

# base case

for j in range(0, W+1):
    if j > w[0]:
        dp[0][j] = v[0]
    else:
        dp[0][j] = 0
for i in range(N):
    dp[i][0] = 0

for i in range(1, N):
    for j in range(1, W+1):
        if j >= w[i]:
            dp[i][j] = max(
                    dp[i-1][j],
                    dp[i-1][j-w[i]] + v[i]
            )
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N-1][W])
