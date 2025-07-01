import sys
input = sys.stdin.readline
INF = float('inf')

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

dp = [[INF]*(1<<N) for _ in range(N)]
dp[K][1<<K] = 0

for mask in range(1<<N):
    for i in range(N):
        if dp[i][mask] == INF:
            continue
        for j in range(N):
            if mask & (1<<j):
                continue
            visit = mask | (1<<j)
            dp[j][visit] = min(dp[j][visit], dp[i][mask] + graph[i][j])
        
answer = INF
for i in range(N):
    answer = min(answer, dp[i][(1<<N)-1])
print(answer)
        
'''
플로이드 워셜로 전체 최소 거리를 구함.
외판원 방문 문제로 치환해서 답 구하기
dp[i][mask] : mask에 포함된 노드를 지나 i번째에 도착했을 때의 최소값
'''