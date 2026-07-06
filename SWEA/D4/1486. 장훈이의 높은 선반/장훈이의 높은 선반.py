TC = int(input())
for tc in range(1, TC+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    heights.sort()
    S = sum(heights)
    dp = [False]*(S+1)
    dp[0] = True
    max_h = 0
    for h in heights:
        for i in range(max_h, -1, -1):
            if dp[i]:
                dp[i+h] = True
        max_h += h
    
    for i in range(B, S+1):
        if dp[i]:
            break
    
    print(f'#{tc} {i-B}')