def solution(n, money):
    MOD = 1_000_000_007
    dp = [0]*(n+1)
    dp[0] = 1
    for val in money:
        for i in range(val, n+1):
            dp[i] += dp[i-val]

    return dp[n]