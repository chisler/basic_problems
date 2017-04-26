


def count(n):
    dp = [0] * (n + 1)

    def walker(n, dp):
        if n < 1:
            return 0

        if dp[n]:
            return dp[n]

        dp[n] = 1 + walker(n-1, dp) + walker(n-2, dp) + walker(n-3, dp)

        return dp[n]

    return walker(n, dp)

print(count(3))