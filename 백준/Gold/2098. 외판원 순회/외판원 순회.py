import sys
input = sys.stdin.readline

N = int(input())

weight = [list(map(int, input().split())) for _ in range(N)]
dp = [[float('inf')]*(1<<N) for _ in range(N)]

dp[0][1<<0] = 0

for mask in range(1<<N):
    for i in range(N):
        if mask | (1<<i) != mask:
            continue
        for next in range(N):
            if mask | (1<<next) == mask:
                continue
            if weight[i][next] == 0:
                continue
            dp[next][mask | (1<<next)] = min(dp[next][mask|(1<<next)], dp[i][mask]+weight[i][next])

answer = float('INF')
for i in range(N):
    if weight[i][0] == 0:
        continue
    answer = min(answer, dp[i][(1<<N)-1] + weight[i][0])
print(answer)

'''
dp[i][mask] : mask의 도시를 거쳐 i번째 도시에 도착한 거리의 최소값
최대 연산 수 : N * (2**N) -> 16* 2**16 -> 2**20 -> 100만
어차피 순환형이기 때문에 시작 노드는 중요하지 않음.
0번 도시부터 시작. 마지막에 0번 도시로 다시 와야함.
dp[next][mask|(1<<next)] = min(본인, dp[i][mask]+weight[i][next]) 
'''