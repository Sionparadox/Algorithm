from collections import deque

directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
def zero_cell(r, c):
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if nr<0 or nr>=N or nc<0 or nc>=N:
            continue
        if board[nr][nc] != '.':
            return False
    return True


def bfs(r, c):
    visited[r][c] = True
    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if visited[nr][nc]:
                continue
            visited[nr][nc] = True
            if zero_cell(nr, nc):
                queue.append((nr, nc))
    
        
        
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    answer = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == '.' and not visited[r][c]:
                if zero_cell(r, c):
                    bfs(r, c)
                    answer += 1
    
    for r in range(N):
        for c in range(N):
            if board[r][c] == '.' and not visited[r][c]:
                answer += 1
    
    print(f'#{tc} {answer}')