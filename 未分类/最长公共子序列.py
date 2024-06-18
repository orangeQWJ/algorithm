A = "Northwestern Polytechnical University"
B = "Massachusetts Institute of Technology"

len_A = len(A)
len_B = len(B)

dp = [[0 for _ in range(len_B)] for _ in range(len_A)]


# base_case
for j in range(len_B):
    if A[0] == B[j]:
        for k in range(j, len_B):
            dp[0][k] = 1
        break
    else:
        dp[0][j] = 0

for i in range(len_A):
    if B[0] == A[i]:
        for k in range(i, len_A):
            dp[i][0] = 1
        break
    else:
        dp[i][0] = 0

# 根据依赖关系,设置遍历顺序
for i in range(1, len_A):
    for j in range(1, len_B):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

max_length = -1
for i in range(len_A):
    for j in range(len_B):
        max_length = max(max_length, dp[i][j])
print(max_length)
