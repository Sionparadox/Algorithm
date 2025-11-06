import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())
board = [input().strip() for _ in range(H)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(r, c):
    queue = deque([(r, c, 0)])
    visited = [[False]*W for _ in range(H)]
    visited[r][c] = True
    while queue:
        r, c, dist = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=H or nc<0 or nc>=W:
                continue
            if board[nr][nc] == 'W' or visited[nr][nc]:
                continue
            visited[nr][nc] = True
            queue.append((nr, nc, dist+1))
    return dist

answer = 0
for r in range(H):
    for c in range(W):
        if board[r][c] == 'W': continue
        answer = max(answer, BFS(r, c))
print(answer)
        
'''
보드에 칸별로 방문체크
방문 안된 'L'칸은 BFS로 탐색 해당칸에서 가장 먼 좌표를 구함.
이후 해당 좌표에 대해 BFS를 돌려서 답 구하기
-> 땅에 사이클이 발생할 경우 오답
'''