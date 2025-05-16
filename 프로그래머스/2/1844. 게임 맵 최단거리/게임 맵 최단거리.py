from collections import deque
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = [[-1]*M for _ in range(N)]
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 1
    while queue:
        r, c = queue.popleft()
        
        for dr, dc in d:
            nr = r+dr
            nc = c+dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if visited[nr][nc] != -1 or maps[nr][nc] == 0:
                continue
            if nr == N-1 and nc == M-1:
                return visited[r][c] + 1
            queue.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1
    return visited[N-1][M-1]
