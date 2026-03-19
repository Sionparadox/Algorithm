import sys, heapq
input = sys.stdin.readline
INF = float('inf')

N, M, K = map(int, input().split())
S, D = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))

prefix = [0]
for _ in range(K):
    prefix.append(int(input()) + prefix[-1])


dist = [[INF]*(N+1) for _ in range(N+1)]
dist[S][0] = 0
pq = []
heapq.heappush(pq, (0, S, 0))

def check(node, cnt, cost):
    for i in range(cnt + 1):
        if dist[node][i] <= cost:
            return False
    return True

while pq:
    cost, curr, cnt = heapq.heappop(pq)
    
    if dist[curr][cnt] < cost:
        continue
    
    if cnt >= N: continue

    for nxt, nc in graph[curr]:
        new_cost = cost + nc
        if dist[nxt][cnt+1] > new_cost:
            if check(nxt, cnt, new_cost):
                dist[nxt][cnt+1] = new_cost
                heapq.heappush(pq, (new_cost, nxt, cnt+1))

candidates = []
min_cost = INF
for k in range(1, N+1):
    if dist[D][k] < min_cost:
        candidates.append((k, dist[D][k]))
        min_cost = dist[D][k]

for inc in prefix:
    answer = INF
    for k, cost in candidates:
        answer = min(answer, cost + k * inc)
    print(answer)

'''
다익스트라를 K번 돌리기? <- 30000번 불가능
dist배열에 방문 도로 횟수도 기록
dist[i][k] : i까지 k개의 도로만 사용해서 가는 최소거리
pq : (통행료, 노드, 도로수)

'''