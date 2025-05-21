import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cheese_count = sum(row.count(1) for row in board)

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def update_air():
    # 모든 외부 공기(-1)에서 시작해서 새로운 외부 공기 찾기
    queue = deque()
    # 가장자리에서 시작
    for i in range(N):
        for j in range(M):
            if board[i][j] == -1:
                queue.append((i, j))
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0:
                board[nr][nc] = -1
                queue.append((nr, nc))

# 초기 외부 공기 설정
board[0][0] = -1
update_air()

answer = 0
while cheese_count > 0:
    answer += 1
    melt = []
    
    # 치즈 녹이기
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt = 0
                for dr, dc in directions:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == -1:
                        cnt += 1
                        if cnt >= 2:
                            melt.append((i, j))
                            break
    
    # 치즈 녹이기
    for r, c in melt:
        board[r][c] = 0
    cheese_count -= len(melt)
    
    # 외부 공기 한 번에 업데이트
    update_air()

print(answer)