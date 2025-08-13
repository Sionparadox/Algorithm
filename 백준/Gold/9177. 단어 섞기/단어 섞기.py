import sys
input = sys.stdin.readline

def check(a, b, s):
    N, M = len(a), len(b)
    if len(s) != N+M:
        return False
    
    dp = [[False]*(M+1) for _ in range(N+1)]
    dp[0][0] = True
    for i in range(N+1):
        for j in range(M+1):
            if i>0 and dp[i-1][j] and a[i-1] == s[i+j-1]:
                dp[i][j] = True
            if j>0 and dp[i][j-1] and b[j-1] == s[i+j-1]:
                dp[i][j] = True
    return dp[N][M]
    
N = int(input())
for i in range(1, N+1):
    a, b, s = input().split()
    ans = "yes" if check(a, b, s) else "no"
    print(f'Data set {i}: {ans}')

'''
dp[i][j] : 첫 단어의 문자 i개, 두번째 단어의 문자 j개를 사용해 타겟의 i+j 번째까지 만들 수 있는가

'''