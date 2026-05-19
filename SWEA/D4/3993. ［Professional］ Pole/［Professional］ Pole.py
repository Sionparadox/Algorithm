T = int(input())
for t in range(1, T+1):
    N, L, R = map(int, input().split())
    dp = [[[0]*(R+1) for _ in range(L+1)] for _ in range(N+1)]
    dp[1][1][1] = 1
    for n in range(2, N+1):
        for i in range(1, L+1):
            for j in range(1, R+1):
                dp[n][i][j] = dp[n-1][i-1][j] + dp[n-1][i][j-1] + dp[n-1][i][j] * (n-2)
    
    print(f'#{t} {dp[N][L][R]}')
        


'''
dp[N][L][R] : N개를 사용해서 왼쪽L,오른쪽 R만큼 보일 때 경우의 수
dp[1][1][1] 기준으로 점점 작은 막대를 하나씩 추가한다고 생각

dp[N-1][L-1][R] + dp[N-1][L][R-1] << 우측끝이나 좌측 끝에 추가
dp[N-1][L][R] * (N-2) << 1길이의 막대를 N-1개의 막대 사이에 삽입
'''