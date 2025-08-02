import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    file = list(map(int, input().split()))
    dp = [[0]*(N+1) for _ in range(N+1)]
    prefix = [0]
    for f in file:
        prefix.append(prefix[-1]+f)
    
    for length in range(2, N+1):
        for left in range(1, N-length+2):
            right = left+length-1
            dp[left][right] = float('inf')
            for k in range(left, right):
                val = dp[left][k] + dp[k+1][right] + prefix[right]-prefix[left-1]
                dp[left][right] = min(dp[left][right], val)
    print(dp[1][N])
        
'''
우선순위 큐에 넣어서 작은 값 2개씩 빼서 합쳐서 넣기?
-> 순서를 유지하며 합쳐야 하기에 불가능

dp[l][r] : l~r구간의 최소비용
dp[l][r] = min(dp[l][k]+dp[k+1][r]+l~r까지의 합)
누적합 구해서 O(1)로 접근

'''