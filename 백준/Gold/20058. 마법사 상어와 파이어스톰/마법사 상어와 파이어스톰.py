import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
cmd = list(map(int, input().split()))
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False]*(2**N) for _ in range(2**N)]

def BFS(r, c):
    visited[r][c] = True
    queue = deque([(r, c)])
    cnt = 0
    while queue:
        r, c = queue.popleft()
        cnt += 1
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=2**N or nc<0 or nc>=2**N:
                continue
            if not visited[nr][nc] and board[nr][nc] >0:
                queue.append((nr, nc))
                visited[nr][nc] = True
    return cnt


def rotate(r, c, k):
    L = 2**k
    for depth in range(L//2):
        first = depth
        last = L-1-depth
        for i in range(first, last):
            offset = i - first
            top = board[r + first][c + i]
            # 왼쪽 → 위쪽
            board[r + first][c + i] = board[r + last - offset][c + first]
            # 아래쪽 → 왼쪽
            board[r + last - offset][c + first] = board[r + last][c + last - offset]
            # 오른쪽 → 아래쪽
            board[r + last][c + last - offset] = board[r + i][c + last]
            # 위쪽 → 오른쪽
            board[r + i][c + last] = top

def spell(k):
    L = 2**k
    for r in range(0, 2**N, L):
        for c in range(0, 2**N, L):
            rotate(r, c, k)
    
    candidates = []
    for r in range(2**N):
        for c in range(2**N):
            if board[r][c] == 0:
                continue
            cnt = 0
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<2**N and 0<=nc<2**N and board[nr][nc]:
                    cnt += 1
            if cnt<3:
                candidates.append((r, c))
    
    for r, c in candidates:
        board[r][c] -= 1
    
for k in cmd:
    spell(k)

tot = 0
maxVal = 0
for r in range(2**N):
    for c in range(2**N):
        tot += board[r][c]
        if not visited[r][c] and board[r][c] >0:
            cnt = BFS(r, c)
            maxVal = max(maxVal, cnt)

print(tot)
print(maxVal)