import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
pool = [list(map(int, input().strip())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(r, c, height):
    visited[r][c] = True
    queue = deque([(r, c)])
    canFill = True
    res = 0
    
    while queue:
        r, c = queue.popleft()
        res += height-pool[r][c]
        pool[r][c] = height
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                canFill = False
                continue
            if not visited[nr][nc] and pool[nr][nc] < height:
                queue.append((nr, nc))
                visited[nr][nc] = True
    
    return res if canFill else 0

answer = 0
for h in range(2, 10):
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if pool[i][j] < h and not visited[i][j]:
                answer += BFS(i, j, h)

print(answer)
        

'''
일단 2~9의 높이로 높여가며 채우기
채울 때는 N*M번돌긴해야해 같은 그룹의 수영장인지는 BFS로 체크

'''