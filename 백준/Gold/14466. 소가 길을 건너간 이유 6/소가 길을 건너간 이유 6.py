import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, K, R = map(int, input().split())
road = defaultdict(set)
for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    road[(r1-1, c1-1)].add((r2-1, c2-1))
    road[(r2-1, c2-1)].add((r1-1, c1-1))

cow = []
for _ in range(K):
    r, c = map(int, input().split())
    cow.append((r-1, c-1))
cow_set = set(cow)
visited = [[False]*N for _ in range(N)]

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
cow_group = []
def BFS(r, c):
    visited[r][c] = True
    queue = deque([(r, c)])
    cnt = 1
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if visited[nr][nc] or (nr, nc) in road[(r,c)]:
                continue
            visited[nr][nc] = True
            queue.append((nr, nc))
            if (nr, nc) in cow_set:
                cnt += 1
    return cnt
    
for cr, cw in cow:
    if visited[cr][cw]:
        continue  
    cow_group.append(BFS(cr, cw))
answer = K*(K-1)//2
for cg in cow_group:
    answer -= cg*(cg-1)//2
print(answer)
