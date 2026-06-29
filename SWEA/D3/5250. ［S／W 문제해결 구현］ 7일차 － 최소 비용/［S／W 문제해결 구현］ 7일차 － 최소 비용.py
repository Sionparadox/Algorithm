import heapq
INF = float('inf')
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[INF]*N for _ in range(N)]
    visited[0][0] = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pq = []
    heapq.heappush(pq, (0, 0, 0))
    while pq:
        cost, r, c = heapq.heappop(pq)
        if r == N-1 and c == N-1:
            break
        
        if visited[r][c] < cost:
            continue
        
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            ncost = cost + 1 + max(board[nr][nc] - board[r][c], 0)
            if ncost < visited[nr][nc]:
                visited[nr][nc] = ncost
                heapq.heappush(pq, (ncost, nr, nc))
    
    print(f"#{tc} {visited[N-1][N-1]}")