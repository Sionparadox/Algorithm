import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
A1, A2, B1, B2 = [tuple(map(int, input().split())) for _ in range(4)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solve(P1, P2, Q1, Q2):
    parent = [[False]*(M+1) for _ in range(N+1)]
    for x, y in (Q1, Q2):
        parent[x][y] = True
    res = BFS(P1, P2, parent)
    
    visited = [[False]*(M+1) for _ in range(N+1)]
    x, y = P2
    while not visited[x][y]:
        visited[x][y] = True
        x, y = parent[x][y]

    res += BFS(Q1, Q2, visited)
    return res


def BFS(P1, P2, visited):
    queue = deque([(*P1, 0)])
    visited[P1[0]][P1[1]] = P1
    while queue:
        x, y, d = queue.popleft()
        if (x, y) == P2:
            return d
        
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if nx<0 or nx>N or ny<0 or ny>M:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = (x, y)
            queue.append((nx, ny, d+1))
    return INF

answer = min(solve(A1, A2, B1, B2), solve(B1, B2, A1, A2))
print(answer if answer != INF else "IMPOSSIBLE")