import sys
from collections import deque
input = sys.stdin.readline

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
pos = tuple(x-1 for x in map(int, input().split()))
passenger = [[x-1 for x in list(map(int, input().split()))] for _ in range(M)]

def minDist(sr, sc, er, ec):
    visited = set([(sr, sc)])
    queue = deque([(sr, sc, 0)])
    while queue:
        r, c, res = queue.popleft()
        if (r, c) == (er, ec):
            return res
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if (nr, nc) in visited or board[nr][nc] == 1:
                continue
            
            visited.add((nr, nc))
            queue.append((nr, nc, res+1))
        
    return -1

def nextP(r, c):
    visited = set([(r, c)])
    queue = deque([(r, c)])
    candidates = []
    dist = 0
    if board[r][c] < 0:
        return -board[r][c]-1, 0
    while queue:

        if candidates:
            candidates.sort()
            return candidates[0][2], dist
        
        L = len(queue)
        for _ in range(L):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr<0 or nr>=N or nc<0 or nc>=N:
                    continue
                if (nr, nc) in visited or board[nr][nc] == 1:
                    continue
                
                if board[nr][nc] < 0:
                    candidates.append((nr, nc, -board[nr][nc]-1))
                    
                visited.add((nr, nc))
                queue.append((nr, nc))

        dist += 1        
        
    return -1, -1

for i in range(M):
    p = passenger[i]
    board[p[0]][p[1]] = -i-1

for _ in range(M):
    pidx, used = nextP(*pos)
    if pidx == -1:
        fuel = -1
        break
    fuel -= used
    if fuel<=0:
        fuel = -1
        break
    p = passenger[pidx]
    dist = minDist(*p)
    if dist == -1:
        fuel = -1
        break
    
    fuel -= dist
    if fuel<0:
        fuel = -1
        break
    fuel += dist*2
    board[p[0]][p[1]] = 0
    pos = (p[2], p[3])
    
print(fuel)