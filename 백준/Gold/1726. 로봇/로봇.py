import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
def normalize(r,c,d):
    mapper = [-1, 0, 2, 1, 3]
    return (r-1, c-1, mapper[d])

start = normalize(*map(int, input().split()))
end = normalize(*map(int, input().split()))
directions = [(0, 1), (1, 0), (0, -1), (-1 ,0)] #ESWN

queue = deque([start])
visited = [[[-1]*4 for _ in range(C)] for _ in range(R)]
visited[start[0]][start[1]][start[2]] = 0

while queue:
    r, c, d = queue.popleft()
    cnt = visited[r][c][d]
    
    if (r,c,d) == end:
        print(cnt)
        break
    
    dr, dc = directions[d]
    for k in range(1, 4):
        nr, nc = r+dr*k, c+dc*k
        if nr<0 or nr>=R or nc<0 or nc>=C:
            continue
        if board[nr][nc] == 1:
            break
        if visited[nr][nc][d] == -1:
            visited[nr][nc][d] = cnt+1
            queue.append((nr, nc, d))
        
    for nd in [(d+1)%4, (d-1)%4]:
        if visited[r][c][nd] == -1:
            visited[r][c][nd] = cnt+1
            queue.append((r, c, nd))

'''
BFS로 최소경로 추적
이동을 먼저 큐에 넣기, 방향전환은 그 이후
이동명령 시 1인 칸이 있으면 k=2,3일때도 못가도록 break
'''