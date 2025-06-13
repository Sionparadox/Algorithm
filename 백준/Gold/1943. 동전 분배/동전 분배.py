import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    S = 0
    coins = []
    for _ in range(N):
        coin, cnt = map(int, input().split())
        S += coin*cnt
        k = 1
        while cnt > 0:
            idx = min(k, cnt)
            coins.append(coin*idx)
            cnt -= idx
            k *= 2
    
    if S%2 == 1:
        print(0)
        continue
    
    S = S//2
    dp = [False]*(S+1)
    dp[0] = True
    
    for coin in coins:
        for i in range(S, coin-1, -1):
            dp[i] = dp[i] | dp[i-coin]
    
    print(1 if dp[S] else 0)

'''
동전을 펼쳐서 넣어둠. 500,2 -> [500, 500]
dp[i] : i금액이 가능한가?

어떤식으로든 절반의 금액이 가능하기만 하면 됨
dp[i] = dp[i] | dp[i-coin]
dp[S//2]에 대해 확인
-> 시간초과 발생
동전을 펼치는 방식이 문제.
Bounded Knapsack의 해결 방법 중 개수를 이진법 분할하는 방식으로 개선해야함
500원 13개면 500원 13개를 펼치는게 아니라 500*1, 500*2, 500*4, 500*6 으로 이진분할해서 넣는 방식
'''
