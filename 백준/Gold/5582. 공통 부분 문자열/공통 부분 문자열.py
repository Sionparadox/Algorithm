import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

N = len(s1)
M = len(s2)
dp = [0]*(M+1)
prev = [0]*(M+1)
answer = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if s1[i-1] == s2[j-1]:
            dp[j] = prev[j-1]+1
            answer = max(answer, dp[j])
        else :
            dp[j] = 0
    prev, dp = dp, [0]*(M+1)

print(answer)

'''
dp[i][j] s1 i번째와 s2 j번째까지 최장 공통 문자열의 길이 << 메모리초과

dp, prev 2개 사용 : prev[i] 이전행 i까지 최대길이, dp[i] 지금행 i까지 최대길이
'''