import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
start, target = map(int, input().split())
start, target = start - 1, target - 1
M = int(input())
graph = [[] for _ in range(N)]
for _ in range(M):
    p, c = map(int, input().split())
    graph[p-1].append(c-1)
    graph[c-1].append(p-1)

visited = [False]*(N)
queue = deque([(start, 0)])

answer = -1
while queue:
    curr, cnt = queue.popleft()
    if curr == target:
        answer = cnt
        break
    
    for nxt in graph[curr]:
        if not visited[nxt]:
            visited[nxt] = True
            queue.append((nxt, cnt+1))

print(answer)


'''
노드 수가 적으므로 BFS로 해결 가능할듯
부모-자식 양방향 그래프로 변경
'''