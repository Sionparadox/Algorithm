import sys
input = sys.stdin.readline


N = int(input())
board = [input().strip().split(' ') for _ in range(N)]
teachers = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'T':
            teachers.append((i, j))

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def check():
    for r, c in teachers:
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            while 0<=nr<N and 0<=nc<N:
                if board[nr][nc] == 'S':
                    return False
                if board[nr][nc] == 'O':
                    break
                nr += dr
                nc += dc
    return True

def backTrack(pos, k):
    if k == 3:
        return check()
    
    if pos == N**2:
        return False
    
    for p in range(pos, N**2):
        r = p//N
        c = p%N
        if board[r][c] == 'X':
            board[r][c] = 'O'
            if backTrack(p+1, k+1):
                return True
            board[r][c] = 'X'
    
    return False

print("YES" if backTrack(0, 0) else "NO")
