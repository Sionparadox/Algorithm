TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    SIZE = sum(arr)
    dp = [False]*(SIZE+1)
    dp[0] = True
    for n in arr:
        for i in range(SIZE, n-1, -1):
            dp[i] |= dp[i-n]
    
    print(f'#{tc} {sum(dp)}')