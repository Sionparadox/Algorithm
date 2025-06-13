import sys
input = sys.stdin.readline

N, M = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(M)]

dp = [0]*(N+1)
for date, page in books:
    for i in range(N, date-1, -1):
        dp[i] = max(dp[i], dp[i-date]+page)
        
print(dp[N])
'''
dp[i] : i일동안 읽을 수 있는 최대 페이지 수

'''