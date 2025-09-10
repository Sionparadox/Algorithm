import sys
input = sys.stdin.readline
MOD = 10007

S = input().strip()
L = len(S)
dp = [[0]*L for _ in range(L)]

for i in range(L):
    dp[i][i] = 1

for k in range(1, L):
    for i in range(L-k):
        j = i+k
        dp[i][j] = (dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1])%MOD
        if S[i] == S[j]:
            dp[i][j] = (dp[i][j] + dp[i+1][j-1]+1)%MOD

print(dp[0][L-1])
        
        
'''
dp[i][j] : i~j 사이에 존재하는 팰린드롬이 되는 부분 문자열의 수
dp[i][i] = 1

dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1]

if S[i] == S[j] : (i,j)번째 문자만으로 팰린드롬 구성 가능
dp[i][j] += dp[i+1][j-1] + 1
'''