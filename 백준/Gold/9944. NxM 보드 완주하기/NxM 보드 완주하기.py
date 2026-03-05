import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def backTrack(r, c, move, cell):
    global answer
    if cell == cells:
        answer = min(answer, move)
        return
    if move>=answer:
        return
    
    for dr, dc in directions:
        nr, nc = r, c
        path = []
        while True:
            nr, nc = nr+dr, nc+dc
            if nr<0 or nr>=N or nc<0 or nc>=M:
                break
            if board[nr][nc] == '*' or visited[nr][nc]:
                break
            visited[nr][nc] = True
            path.append((nr, nc))
        
        if path:
            backTrack(nr-dr, nc-dc, move+1, cell+len(path))
            for nr, nc in path:
                visited[nr][nc] = False
        

while True:
    t += 1
    _input = input()
    if not _input :
        break
    N, M = map(int, _input.split())
    board = [list(input().rstrip()) for _ in range(N)]
    cells = sum([row.count('.') for row in board])
    answer = float('inf')
    for r in range(N):
        for c in range(M):
            if board[r][c] == '.':
                visited = [[False]*M for _ in range(N)]
                visited[r][c] = True
                backTrack(r, c, 0, 1)
    
    if answer == float('inf'):
        answer = -1
    print(f'Case {t}: {answer}')
