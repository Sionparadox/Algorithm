import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

visited = [[False]*C for _ in range(R)]
dp = [[-1]*C for _ in range(R)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def DFS(r, c):
    if r<0 or r>=R or c<0 or c>=C or board[r][c] == 'H':
        return 0
    if visited[r][c]:
        print(-1)
        exit(0)
    
    if dp[r][c] != -1:
        return dp[r][c]
    
    visited[r][c] = True
    k = int(board[r][c])
    res = 0
    for dr, dc in directions:
        nr, nc = r+dr*k, c+dc*k
        res = max(res, DFS(nr, nc)+1)
    
    visited[r][c] = False
    
    dp[r][c] = res
    return res
    
    
print(DFS(0,0))

'''
기본적인 로직은 BFS사용
사이클 탐지는 prev에 이전 방문위치 기억하도록 해서 같을 경우 사이클 탐지
-> 실패
전체 경로를 탐색하도록 DFS로 변경
사이클 처리는 백트래킹처럼 visited의 True, False 사이에 재귀 호출로 사이클 탐색
dp[r][c] : r,c칸에서 움직일 수 있는 최대횟수
'''