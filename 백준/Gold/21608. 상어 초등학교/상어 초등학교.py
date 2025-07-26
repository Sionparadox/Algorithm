import sys
input = sys.stdin.readline

N = int(input())
board = [[0]*N for _ in range(N)]
favor = [None]*(N**2+1)

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def sit(n):
    candidates = []
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:            
                blank = 0
                want = 0
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr<0 or nr>=N or nc<0 or nc>=N:
                        continue
                    if board[nr][nc] == 0:
                        blank += 1
                    elif board[nr][nc] in favor[n]:
                        want += 1
                candidates.append((-want, -blank, r, c))
    candidates.sort()
    _, _, r, c = candidates[0]
    board[r][c] = n

for _ in range(N**2):
    n, *arr = list(map(int, input().split()))
    favor[n] = set(arr)
    sit(n)

answer = 0
for r in range(N):
    for c in range(N):
        n = board[r][c]
        cnt = 0
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<N and board[nr][nc] in favor[n]:
                cnt += 1
        if cnt != 0:
            answer += 10**(cnt-1)
    
print(answer)