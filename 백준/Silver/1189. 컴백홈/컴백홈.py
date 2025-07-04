import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

visited = [[False]*C for _ in range(R)]
visited[R-1][0] = True
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = 0
def backTrack(r, c, k):
    global answer
    if r == 0 and c == C-1:
        if k == K:
            answer += 1
        return
    if k >= K:
        return
    
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if nr<0 or nr>=R or nc<0 or nc>=C:
            continue
        if visited[nr][nc] or board[nr][nc] == 'T':
            continue
        
        visited[nr][nc] = True
        backTrack(nr, nc, k+1)
        visited[nr][nc] = False

backTrack(R-1, 0, 1)
print(answer)