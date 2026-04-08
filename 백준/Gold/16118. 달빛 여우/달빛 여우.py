import sys, heapq
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, d = map(int, input().split())
    graph[u].append((v, d*2))
    graph[v].append((u, d*2))

dist = [INF]*(N+1)
dist[1] = 0

pq = [(0, 1)]
while pq:
    d, curr = heapq.heappop(pq)
    
    if dist[curr]<d:
        continue
    
    for nxt, nd in graph[curr]:
        new_d = d+nd
        if dist[nxt] > new_d:
            dist[nxt] = new_d
            heapq.heappush(pq, (new_d, nxt))

wolf = [[INF]*2 for _ in range(N+1)]
wolf[1][0] = 0
pq = [(0, 1, 0)]

while pq:
    d, curr, state = heapq.heappop(pq)
    
    if wolf[curr][state] < d:
        continue
    
    for nxt, nd in graph[curr]:
        if state == 0:
            new_d = d + nd//2
        else:
            new_d = d + nd*2
        
        new_state = 1-state
        if wolf[nxt][new_state] > new_d:
            wolf[nxt][new_state] = new_d
            heapq.heappush(pq, (new_d, nxt, new_state))

            
        

answer = 0
for i in range(1, N+1):
    if dist[i] < min(wolf[i]):
        answer += 1

print(answer)

'''
늑대는 dist를 2차원으로 만들어서 다음에 뛸지 걸을지 저장
'''
