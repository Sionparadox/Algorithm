INF = float('inf')
def solution(strs, t):
    L = len(t)
    dp = [INF]*(L+1)
    dp[0] = 0
    strs_set = set(strs)
    maxLen = max(len(s) for s in strs)
    for i in range(1, L+1):
        for l in range(1, maxLen+1):
            if i<l:
                continue
            if t[i-l:i] in strs_set:
                dp[i] = min(dp[i], dp[i-l]+1)

    return dp[L] if dp[L] != INF else -1