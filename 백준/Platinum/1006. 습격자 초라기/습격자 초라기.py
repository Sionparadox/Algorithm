import sys
input = sys.stdin.readline
INF = float('inf')


def solve(k):
    
    dp = [[INF] * 3 for _ in range(N)]
    
    if k == 0:
        dp[0][0] = 1
        dp[0][1] = 1
        dp[0][2] = 1 if enemies[0][0] + enemies[1][0] <= W else 2
    elif k == 1:
        dp[0][0] = 0             
        dp[0][2] = 1
    elif k == 2:
        dp[0][1] = 0
        dp[0][2] = 1
    elif k == 3:
        dp[0][2] = 0 
    
    for i in range(1, N):
        
        dp[i][0] = dp[i-1][2] + 1
        if enemies[0][i] + enemies[0][i-1] <= W:
            dp[i][0] = min(dp[i][0], dp[i-1][1]+1)
        
        dp[i][1] = dp[i-1][2] + 1
        if enemies[1][i] + enemies[1][i-1] <= W:
            dp[i][1] = min(dp[i][1], dp[i-1][0]+1)
            
        if enemies[0][i] + enemies[1][i] <= W:
            dp[i][2] = dp[i-1][2] + 1
        else:
            dp[i][2] = dp[i-1][2] + 2 
        
        dp[i][2] = min(dp[i][2], dp[i][0]+1, dp[i][1]+1)
        
        if enemies[0][i] + enemies[0][i-1] <= W and enemies[1][i] + enemies[1][i-1] <= W:
            if i>=2:
                dp[i][2] = min(dp[i][2], dp[i-2][2] + 2)
            elif k == 0:
                dp[i][2] = min(dp[i][2], 2)
    
    if k == 0:
        return dp[N-1][2]
        
    if k == 1:
        return dp[N-1][1] + 1
    
    if k == 2:
        return dp[N-1][0] + 1
            
    return dp[N-2][2] + 2
    


T = int(input())    
for _ in range(T):
    N, W = map(int, input().split())
    enemies = [list(map(int, input().split())) for _ in range(2)]
    
    if N == 1:
        print(1 if enemies[0][0] + enemies[1][0] <= W else 2)
        continue
    
    answer = solve(0)
    if enemies[0][0] + enemies[0][N-1] <= W:
        answer = min(answer, solve(1))
    
    if enemies[1][0] + enemies[1][N-1] <= W:
        answer = min(answer, solve(2))
        
    if enemies[0][0] + enemies[0][N-1] <= W and enemies[1][0] + enemies[1][N-1] <= W:
        answer = min(answer, solve(3))
        
    print(answer)

'''
N-1번과 0번이 인접한 dp
dp[i][state] : i번째까지 필요한 최소 부대 수, state(0: 0번줄만 채움, 1: 1번줄만 채움, 2: 둘다 채움)
state 0: 이전 열의 0번칸과 동일한 소대 배치 or 새로운 소대 하나 배치
state 1: 이전 열의 1번칸과 동일한 소대 배치 or 새로운 소대 하나 배치
state 2: 1) 현재 열 2개칸에 하나의 소대 배치
         2) 0번은 이전이랑 묶고 1번은 따로 배치
         3) 1번은 이전이랑 묶고 0번은 따로 배치
         4) 0,1번 둘다 이전이랑 묶기

0,N-1번 열을 4가지 경우에 대해 solve
- 두 열이 간섭x (선형)
- 0번칸만 두 열이 공유
- 1번칸만 두 열이 공유
- 두칸 다 두 열이 공유
'''