from collections import deque
T = int(input())
for t in range(1, T+1):
    N = int(input())
    maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    visited = [[-1]*N for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                queue.append((r, c))
                visited[r][c] = 0
                break
        if queue:
            break
    answer = 0
    while queue:
        r, c = queue.popleft()
        k = visited[r][c]
        if maze[r][c] == 3:
            answer = k-1
            break
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if visited[nr][nc] != -1 or maze[nr][nc] == 1:
                continue
            visited[nr][nc] = k+1
            queue.append((nr, nc))
    
    print(f'#{t} {answer}')