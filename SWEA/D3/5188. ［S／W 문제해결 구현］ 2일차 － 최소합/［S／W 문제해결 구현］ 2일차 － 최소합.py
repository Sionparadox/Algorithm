from collections import deque
INF = float('inf')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dist = [[INF]*N for _ in range(N)]
    queue = deque([(0, 0)])
    dist[0][0] = board[0][0]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            nd = dist[r][c] + board[nr][nc]
            if dist[nr][nc] > nd:
                dist[nr][nc] = nd
                queue.append((nr, nc))
    
    print(f'#{t} {dist[N-1][N-1]}')