import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    r1, c1, r2, c2 = map(int, input().split())
    graph[(r1, c1)].append((r2, c2))

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
light = [[False]*(N+1) for _ in range(N+1)]
visited = [[False]*(N+1) for _ in range(N+1)]
light[1][1] = True
visited[1][1] = True
queue = deque([(1, 1)])
answer = 1

while queue:
    r, c = queue.popleft()
    
    for gr, gc in graph[(r, c)]:
        if not light[gr][gc]:    
            light[gr][gc] = True
            answer += 1
            for dr, dc in directions:
                nr, nc = gr+dr, gc+dc
                if nr<1 or nr>N or nc<1 or nc>N:
                    continue
                if visited[nr][nc]:
                    queue.append((gr, gc))
                    visited[gr][gc] = True
                    break
    
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if nr<1 or nr>N or nc<1 or nc>N:
            continue
        if not visited[nr][nc] and light[nr][nc]:
            queue.append((nr, nc))
            visited[nr][nc] = True
        
        
print(answer)