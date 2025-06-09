import sys
from collections import deque, defaultdict
import heapq
input = sys.stdin.readline
INF = float('inf')

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    S, D = map(int, input().split())
    graph = defaultdict(list)
    reversed_graph = defaultdict(list)
    for _ in range(M):
        u, v, p = map(int, input().split())
        graph[u].append((v, p))
        reversed_graph[v].append((u, p))

    #다익스트라
    dist = [INF]*N
    dist[S] = 0
    pq = []
    heapq.heappush(pq, (0, S))
    while pq:
        w, curr = heapq.heappop(pq)
        
        if w > dist[curr]:
            continue
        
        for next, weight in graph[curr]:
            nw = w+weight
            if dist[next] > nw:
                dist[next] = nw
                heapq.heappush(pq, (nw, next))

    #역추적
    queue = deque([D])
    disabled = [[False]*N for _ in range(N)]
    while queue:
        curr = queue.popleft()
        for pre, weight in reversed_graph[curr]:
            if dist[curr] == dist[pre]+weight and not disabled[pre][curr]:
                disabled[pre][curr] = True
                queue.append(pre)
    
    pq = []
    dist = [INF]*N
    dist[S] = 0
    heapq.heappush(pq, (0, S))
    while pq:
        w, curr = heapq.heappop(pq)
        
        if w > dist[curr]:
            continue
        
        for next, weight in graph[curr]:
            nw = w+weight
            if dist[next] > nw and not disabled[curr][next]:
                dist[next] = nw
                heapq.heappush(pq, (nw, next))
    
    print(dist[D] if dist[D] != INF else -1)


'''
다익스트라 두번 돌리기
한번 돌려서 역추적으로 최단 경로 전부 disabled에 넣고
두번째에는 disabled에 없는 길로만 가기
## prev 배열로 역추적 시에는 시간초과가 나버림
역방향 그래프를 만들어서 추적하도록 변경

'''