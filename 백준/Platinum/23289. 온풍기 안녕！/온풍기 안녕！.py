import sys
from collections import deque, defaultdict
input = sys.stdin.readline

R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)] 
testcase = []
heater = []
for r in range(R):
    for c in range(C):
        if board[r][c] == 5:
            testcase.append((r, c))
        elif board[r][c] != 0:
            heater.append((r, c, board[r][c]-1))


walls = defaultdict(set)
W = int(input())
for _ in range(W):
    x, y, t = map(int, input().split())
    x, y = x-1, y-1
    walls[(x, y)].add((x-(1-t), y+t))
    walls[(x-(1-t), y+t)].add((x, y))

room = [[0]*C for _ in range(R)]

def wind(r, c, d):
    dr, dc = directions[d]
    queue = deque([(r+dr, c+dc, 5)])
    visited = set()
    while queue:
        r, c, t = queue.popleft()
        room[r][c] += t
        if t == 1:
            continue
        for k in (-1, 0, 1):
            nr, nc = r+dr+dc*k, c+dc+dr*k
            if nr<0 or nr>=R or nc<0 or nc>=C:
                continue
            if (nr, nc) in visited:
                continue
            if (r, c) in walls[(r+dc*k, c+dr*k)] or (nr, nc) in walls[(r+dc*k, c+dr*k)]:
                continue
            visited.add((nr, nc))
            queue.append((nr, nc, t-1))
            
def adjust():
    res = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if r<R-1:
                if (r+1, c) not in walls[(r, c)]:
                    val = abs(room[r][c]-room[r+1][c])//4
                    if room[r][c] > room[r+1][c]:
                        val *= -1
                    res[r][c] += val
                    res[r+1][c] -= val
            if c<C-1:
                if (r, c+1) not in walls[(r, c)]:
                    val = abs(room[r][c]-room[r][c+1])//4
                    if room[r][c] > room[r][c+1]:
                        val *= -1
                    res[r][c] += val
                    res[r][c+1] -= val
                        
    for r in range(R):
        for c in range(C):
            room[r][c] += res[r][c]
            if r in (0,R-1) or c in (0, C-1):
                room[r][c] = max(0, room[r][c]-1)

def check():
    for r, c in testcase:
        if room[r][c] < K:
            return False
    return True


chocolate = 0
while chocolate<=100:
    for r, c, d in heater:
        wind(r, c, d)
    adjust()
    chocolate += 1
    if check():
        break
    
print(chocolate)