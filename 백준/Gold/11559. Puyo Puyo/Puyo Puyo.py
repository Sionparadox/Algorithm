import sys
from collections import deque
input = sys.stdin.readline

board = [input().rstrip() for _ in range(12)]
board = list(map(list, zip(*board[::-1])))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def connected(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True
    key = board[r][c]
    res = []
    
    while queue:
        r, c = queue.popleft()
        res.append((r, c))
        for dr, dc in directions:
            nr, nc = r+dr ,c+dc
            if nr<0 or nr>=6 or nc<0 or nc>=12:
                continue
            if visited[nr][nc] or board[nr][nc] != key:
                continue
            visited[nr][nc] = True
            queue.append((nr, nc))
    return res

def fall(arr):
    removed = set(arr)
    for r in range(6):
        row = [x for i, x in enumerate(board[r]) if (r, i) not in removed]
        row = row + ['.']*(12-len(row))
        board[r] = row

answer = 0

while True:
    visited = [[False]*12 for _ in range(6)]
    blocks = []
    for r in range(6):
        for c in range(12):
            if board[r][c] != '.' and not visited[r][c]:
                tmp = connected(r, c)
                if len(tmp) >=4:
                    blocks.extend(tmp)
    if len(blocks) == 0:
        break
    
    fall(blocks)
    answer += 1

print(answer)
