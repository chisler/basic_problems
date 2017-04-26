def coins(n):

    cs = [1, 5, 10, 25]
    dp = [1] + [0] * n

    for coin in cs:
        for i in range(coin, n + 1):
            dp[i] += dp[i-coin]

    return dp[n]

print(coins(10))