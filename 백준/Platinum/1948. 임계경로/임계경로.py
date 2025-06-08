import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N)]
indegree = [0]*N
reversed_graph = [[] for _ in range(N)]
for _ in range(M):
    s, e, t = map(int, input().split())
    s -= 1
    e -= 1
    graph[s].append((e, t))
    reversed_graph[e].append((s, t))
    indegree[e] += 1

start, end = map(int, input().split())
start -= 1
end -= 1

queue = deque([start])

time = [0]*N
while queue:
    node = queue.popleft()

    for next, t in graph[node]:
        if time[next] < time[node] + t:
            time[next] = time[node] + t
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

maxTime = time[end]
visited = [False]*N
cnt = 0
queue = deque([end])

while queue:
    node = queue.popleft()
    
    for prev, t in reversed_graph[node]:
        if time[prev]+t == time[node]:
            cnt += 1
            if not visited[prev]:
                visited[prev] = True
                queue.append(prev)

print(maxTime)
print(cnt)

'''
기본적으로는 위상정렬 + time 배열을 갱신하며 가는 느낌.
지금 걸린 시간이 이전에 온 시간보다 크면 바꿔버리기(최대 비용 경로 저장)

이후 역방향 그래프에 대해 BFS 
-> 시간을 비교해서 최대시간을 지나는 경로인지 탐색.
'''
    
