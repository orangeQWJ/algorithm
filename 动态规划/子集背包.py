def main():
    w = [1, 5, 11, 5]
    w = [1, 3, 2, 5, 11]

    W = sum(w)/2
    if W != sum(w)//2:
        print(False)
        return False
    else:
        W = int(W)
    # i max value len(w)-1,
    # j max value W
    dp = [[False] * (W+1) for _ in range(len(w))]

    for i in range(len(w)):
        dp[i][0] = True

    for j in range(W+1):
        if w[0] == j:
            dp[0][j] = True
    dp[0][0] = True

    for i in range(1, len(w)):
        for j in range(1, W+1):
            if j >= w[i]:
                dp[i][j] = dp[i-1][j-w[i]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[len(w)-1][W])


main()
