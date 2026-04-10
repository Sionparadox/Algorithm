import sys, heapq
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
price = [INF]+list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))

dist = [[INF]*(N+1) for _ in range(N+1)]
pq = [(0, 1, 1)]

while pq:
    cost, curr, min_node = heapq.heappop(pq)
    if curr == N:
        print(cost)
        break
        
    if dist[curr][min_node] < cost:
        continue
    
    for nxt, d in graph[curr]:
        new_cost = cost + d * price[min_node]
        
        new_min_node = min_node
        if price[nxt] < price[min_node]:
            new_min_node = nxt
        
        if dist[nxt][new_min_node] > new_cost:
            dist[nxt][new_min_node] = new_cost
            heapq.heappush(pq, (new_cost, nxt, new_min_node))



'''
dist를 갱신할 때 이전노드에서 현재노드까지 거리 * 현재까지 경로 중 최저가
pq에 (cost, node, min_price_node)를 집어넣음
dist[node][min_price_node] 형식
<< 가격으로 배열을 만들면 무의미한 가격 구간이 생겨버림
'''