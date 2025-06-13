import sys
input = sys.stdin.readline

while True:
    N, M = map(float, input().split())
    N = int(N)
    M = int(round(M*100))
    if N == 0 and M == 0:
        break
    calory = [0]*N
    money = [0]*N
    for i in range(N):
        c, p = map(float, input().split())
        calory[i] = int(c)
        money[i] = int(round(p*100))

    dp = [0]*(M+1)
    
    for k in range(N):
        cal = calory[k]
        pay = money[k]
        for i in range(pay, M+1):
            dp[i] = max(dp[i], dp[i-pay]+cal)
    
    print(dp[M])


'''
dp[i] : i원으로 얻을 수 있는 최대 칼로리
unbounded Knapsack

'''