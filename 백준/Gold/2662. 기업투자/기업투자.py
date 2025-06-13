import sys
input = sys.stdin.readline

N, M = map(int, input().split())

profit = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    cost = list(map(int, input().split()))
    profit[i][1:] = cost[1:]

dp = [[0]*(M+1) for _ in range(N+1)]
invest = [[0]*(M+1) for _ in range(N+1)]

for j in range(1, M+1):
    for i in range(N+1):
        for k in range(i+1):
            if dp[i][j] < dp[i-k][j-1]+profit[k][j]:
                dp[i][j] = dp[i-k][j-1]+profit[k][j]
                invest[i][j] = k

money = N
res = []
for i in range(M, 0, -1):
    temp = invest[money][i]
    res.append(temp)
    money -= temp
print(dp[N][M])
print(' '.join(map(str, reversed(res))))

'''
dp[i][j] : 1~j번째기업에 i원 투자했을 때 이익
ex) dp[3][4] : 1~4번째 기업에 3만원을 분배하여 투자했을 때 최대이익
i,j에 대해 탐색하며 dp[i][j] = max(dp[i][j], dp[i-k][j-1]+profit[k][j])
: 1~j번째기업에 i원 투자했을 때 이익 = 이전 기업까지 k금액 빼고 투자했을 때의 이익 + 현재 기업에 k금액 투자했을 때 이익
갱신될 때 invest[i][j] = k  (역추적용)
가장 나중 번호의 기업을 고려해서 값이 결정되므로 invest 배열 순회는 역방향으로 해야함
'''