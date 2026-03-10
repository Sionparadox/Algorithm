import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
parent = [i for i in range(K + 1)]
lands = [[0] * N for _ in range(N)]
queue = deque()

for i in range(1, K + 1):
    r, c = map(int, input().split())
    lands[r-1][c-1] = i
    queue.append((r-1, c-1))

def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    u, v = find(u), find(v)
    if u != v:
        parent[v] = u
        return True
    return False

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

cnt = 0

temp_q = list(queue)
for r, c in temp_q:
    current_civ = lands[r][c]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            neighbor_civ = lands[nr][nc]
            if neighbor_civ != 0 and neighbor_civ != current_civ:
                if union(current_civ, neighbor_civ):
                    cnt += 1

if cnt == K - 1:
    print(0)
    exit(0)

answer = 0
while queue:
    
    for _ in range(len(queue)):
        r, c = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if lands[nr][nc] == 0:
                    lands[nr][nc] = lands[r][c]
                    queue.append((nr, nc))
                    
                    for dr, dc in directions:
                        nnr, nnc = nr + dr, nc + dc
                        if 0 <= nnr < N and 0 <= nnc < N:
                            if lands[nnr][nnc] != 0 and lands[nnr][nnc] != lands[nr][nc]:
                                if union(lands[nr][nc], lands[nnr][nnc]):
                                    cnt += 1
    
    answer += 1
    
    if cnt == K - 1:
        print(answer)
        break