import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
def move(d, s, clouds):
    res = []
    dr, dc = directions[d]
    for r, c in clouds:
        res.append(((r+dr*s)%N, (c+dc*s)%N))

    return res

def make(clouds):
    res = []
    cloudSet = set(clouds)
    for r in range(N):
        for c in range(N):
            if board[r][c] >= 2 and (r, c) not in cloudSet:
                res.append((r, c))
                board[r][c] -= 2
    return res

for _ in range(M):
    d, s = map(int, input().split())
    clouds = move(d-1, s, clouds)
    for r, c in clouds:
        board[r][c] += 1
    
    for r, c in clouds:
        for dr, dc in directions[1::2]:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<N and board[nr][nc]>0:
                board[r][c] += 1
    
    clouds = make(clouds)

print(sum(sum(row) for row in board))    
            