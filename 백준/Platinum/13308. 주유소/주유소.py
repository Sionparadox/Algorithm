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

memo_price = [INF]*(N+1)
pq = [(0, 1, price[1])]

while pq:
    cost, curr, min_price = heapq.heappop(pq)
    if curr == N:
        print(cost)
        break
        
    if memo_price[curr] <= min_price:
        continue
    memo_price[curr] = min_price
    
    for nxt, d in graph[curr]:
        new_cost = cost + d * min_price
        new_min_price = min(min_price, price[nxt])
        heapq.heappush(pq, (new_cost, nxt, new_min_price))



'''
dist를 갱신할 때 이전노드에서 현재노드까지 거리 * 현재까지 경로 중 최저가
pq에 (cost, node, min_price_node)를 집어넣음
dist[node][min_price_node] 형식
<< 가격으로 배열을 만들면 무의미한 가격 구간이 생겨버림
-> early return을 적용해서 AC

1차원배열로 최적화 가능?
현재 노드포함 이전 경로까지의 최저가를 기록해서 이보다 크면 탐색 x

'''