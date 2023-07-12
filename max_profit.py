def max_profit(coins):
    n = len(coins)
    dp = [[0] * n for _ in range(n)]

    for gap in range(n):
        for i in range(n - gap):
            j = i + gap
            if gap == 0:
                dp[i][j] = coins[i]
            elif gap == 1:
                dp[i][j] = max(coins[i], coins[j])
            else:
                choose_start = coins[i] + min(dp[i+2][j], dp[i+1][j-1])
                choose_end = coins[j] + min(dp[i][j-2], dp[i+1][j-1])
                dp[i][j] = max(choose_start, choose_end)
            if gap > 1:
                print(gap, i, j, choose_start, choose_end, coins[i], coins[j])
                for i in range(len(dp)):
                    print(dp[i])
                print()
    return dp[0][n-1]

coins = [10, 20, 5, 4]
max_profit = max_profit(coins)
print(max_profit)  # Output: 12
