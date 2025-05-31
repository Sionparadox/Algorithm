import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def DFS(r, c):
    if dp[r][c] != 0:
        return dp[r][c]
    
    dp[r][c] = 1
    for dr, dc in directions:
        nr = r+dr
        nc = c+dc
        if 0<=nr<N and 0<=nc<N and forest[nr][nc] > forest[r][c]:
            dp[r][c] = max(dp[r][c], DFS(nr, nc)+1)
    
    return dp[r][c]

answer = 0
for i in range(N):
    for j in range(N):
        answer = max(answer, DFS(i, j))

print(answer)