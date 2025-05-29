import sys
input = sys.stdin.readline
MOD = 1000007

M = int(input())

dp = [0]*(M+1)
dp[0] = dp[1] = 1
for i in range(2, M+1):
    dp[i] = (dp[i-1] + dp[i-2])%MOD
print(dp[M-1])



# dp = [[0,0] for _ in range(M+1)]
# dp[0][0] = 0
# dp[0][1] = 1

# for i in range(M):
    # dp[i+1][0] = (dp[i][0] + dp[i][1])%MOD
    # dp[i+1][1] = dp[i][0]%MOD

# print(sum(dp[M-1])%MOD)
'''
dp[i][0] : i번 연산으로 1이 되는 짝수의 개수
dp[i][1] : i번 연산으로 1이 되는 홀수의 개수
dp[i+1][0] = dp[i][0] + dp[i][1]   //2를 곱하는 연산이기 때문에 
dp[i+1][1] = dp[i][0] //짝수에만 1을 빼는 연산이 가능
1번 : 2
2번 : 4
3번 : 8, 3
4번 : 16, 7, 6
5번 : 32, 15, 14, 12, 5
6번 : 64, 31, 30, 28, 13, 24, 11, 10

'''

