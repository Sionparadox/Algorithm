import sys
from collections import deque
input = sys.stdin.readline

N , M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
vector = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def move(r, c, dir):
    cnt = 0
    dr, dc = dir
    while board[r+dr][c+dc] != '#' and board[r][c] != 'O':
        r += dr
        c += dc
        cnt += 1
    return r, c, cnt

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            redPos = (i, j)
        if board[i][j] == 'B':
            bluePos = (i,j)

queue = deque()
visited[redPos[0]][redPos[1]][bluePos[0]][bluePos[1]] = True
queue.append((redPos, bluePos, 0))

answer = -1
while queue and answer == -1:
    red, blue, depth = queue.popleft()
    if depth >= 10 :
        break
    for dir in vector:
        rx, ry, rCnt = move(red[0],red[1], dir)
        bx, by, bCnt = move(blue[0], blue[1], dir)
        if board[bx][by] == 'O':
            continue
        if board[rx][ry] == 'O':
            answer = depth+1
            break
        
        if rx==bx and ry==by:
            if rCnt > bCnt:
                rx -= dir[0]
                ry -= dir[1]
            else :
                bx -= dir[0]
                by -= dir[1]
        
        if not visited[rx][ry][bx][by]:
            visited[rx][ry][bx][by] = True
            queue.append(((rx, ry), (bx, by), depth+1))
            
print(answer)
'''
visited[red_r][red_c][blue_r][blue_c]

'''