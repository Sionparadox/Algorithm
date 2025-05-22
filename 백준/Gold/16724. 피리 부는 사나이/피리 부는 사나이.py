import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
command = [list(input().strip()) for _ in range(N)]
directions = {
    'U' : (-1, 0),
    'D' : (1, 0),
    'L' : (0, -1),
    'R' : (0, 1)
}
visited = [[False]*M for _ in range(N)]
arrived = [[False]*M for _ in range(N)]
answer = 0
def DFS(r, c, path):
    global answer
    visited[r][c] = True
    path.add((r,c))
    dr, dc = directions[command[r][c]]
    nr = r+dr
    nc = c+dc
    
    if not visited[nr][nc]:
        DFS(nr, nc, path)
    elif not arrived[nr][nc]:
        answer += 1
    
    for x, y in path:
        arrived[x][y] = True   

for r in range(N):
    for c in range(M):
        if not visited[r][c]:
            DFS(r, c, set())

print(answer)