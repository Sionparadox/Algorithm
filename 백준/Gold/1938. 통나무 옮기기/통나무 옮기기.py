import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
L = N**2
visited = [[[False]*2 for _ in range(N)] for _ in range(N)]
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

B = []
E = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 'B':
            B.append((r, c))
        elif board[r][c] == 'E':
            E.append((r, c))

sr, sc = B[1]
er, ec = E[1]

sd = 0 if B[0][0] == B[1][0] else 1
ed = 0 if E[0][0] == E[1][0] else 1
            

def can_rotate(r, c, v):
    if visited[r][c][1-v]:
        return False
    
    for dr in [-1, 0, 1]:
        for dc in [-1, 0 ,1]:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=N:
                return False
            if board[nr][nc] == '1':
                return False
    
    return True

def can_move(r, c, v, d):
    dr, dc = directions[d]
    nr, nc = r+dr, c+dc
    if nr<0 or nr>=N or nc<0 or nc>=N:
        return False
    if visited[nr][nc][v]:
        return False
    
    if v == 0:
        for dc in [-1, 0, 1]:
            _nc = nc+dc
            if _nc<0 or _nc>=N:
                return False
            if board[nr][_nc] == '1':
                return False
    else:
        for dr in [-1, 0, 1]:
            _nr = nr+dr
            if _nr<0 or _nr>=N:
                return False
            if board[_nr][nc] == '1':
                return False
    
    return True
        

queue = deque([(sr, sc, sd)])
visited[sr][sc][sd] = True
answer = 0
while queue:
    for _ in range(len(queue)):
        r, c, v = queue.popleft()
        if (r, c, v) == (er, ec ,ed):
            print(answer)
            exit(0)
        
        if can_rotate(r, c ,v):
            visited[r][c][1-v] = True
            queue.append((r, c ,1-v))
        
        for d in range(4):
            if can_move(r, c, v, d):
                nr, nc = r+directions[d][0], c+directions[d][1]
                visited[nr][nc][v] = True
                queue.append((nr, nc, v))
    answer += 1
print(0)   

'''
visited : 중심 좌표 + 가로/세로 로 저장(가로 0)
'''
    