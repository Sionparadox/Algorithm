import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True
    res = set([(r, c)])
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            if visited[nr][nc] or board[nr][nc] == 0:
                continue
            
            visited[nr][nc] = True
            queue.append((nr, nc))
            res.add((nr, nc))
    
    return res

def distance(x, y):
    A = islands[x]
    B = islands[y]
    res = float('inf')
    
    min_r1 = min(r for r,_ in A)
    max_r1 = max(r for r,_ in A)
    min_c1 = min(c for _,c in A)
    max_c1 = max(c for _,c in A)
    
    min_r2 = min(r for r,_ in B)
    max_r2 = max(r for r,_ in B)
    min_c2 = min(c for _,c in B)
    max_c2 = max(c for _,c in B)
    
    start_r = max(min_r1, min_r2)
    end_r = min(max_r1, max_r2)
    start_c = max(min_c1, min_c2)
    end_c = min(max_c1, max_c2)
    
    if start_r <= end_r:
        for row in range(start_r, end_r+1):
            cols1 = [c for r, c in A if r == row]
            cols2 = [c for r, c in B if r == row]
            for c1 in cols1:
                for c2 in cols2:
                    if abs(c1-c2)>2:
                        s, e = sorted([c1, c2])
                        if all(board[row][col] == 0 for col in range(s+1, e)):
                            res = min(res, e-s-1)
    
    if start_c <= end_c:
        for col in range(start_c, end_c+1):
            rows1 = [r for r, c in A if c == col]
            rows2 = [r for r, c in B if c == col]
            for r1 in rows1:
                for r2 in rows2:
                    if abs(r1-r2)>2:
                        s, e = sorted([r1, r2])
                        if all(board[row][col] == 0 for row in range(s+1, e)):
                            res = min(res, e-s-1)
    
    return res
    
def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    u = find(u)
    v = find(v)
    if u == v:
        return False
    parent[v] = u
    return True

islands = []
for i in range(N):
    for j in range(M):
        if not visited[i][j] and board[i][j] == 1:
            island = BFS(i, j)
            islands.append(island)

K = len(islands)
bridges = []
for i in range(K-1):
    for j in range(i+1, K):
        d = distance(i, j)
        if d != float('inf'):
            bridges.append((d, i, j))

bridges.sort()
parent = [x for x in range(K)]
answer = 0
cnt = 0
for d, u, v in bridges:
    if union(u, v):
        answer += d
        cnt += 1
        if cnt == K-1:
            break

print(answer if cnt == K-1 else -1)

'''
BFS로 섬을 찾아서 좌표를 모아서 섬을 인덱싱
이후 두 섬간의 거리를 구함.
row, col 각각 최대, 최소를 저장해서 겹치는지 구한 후 겹친다면 중간에 섬이 없는지 해당 행,열에 대해 검사.
2보다 큰 최소거리를 반환
이후 거리 순으로 오름차순 정렬하고
union-find활용해서 모든 다리에 대해 탐색
연결 횟수를 저장해서 K-1인지 비교
'''