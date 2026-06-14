directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (1, 1), (-1, 1), (-1, -1)]
def put(x, y, color):
    board[x][y] = color
    enemy = 1-color
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        candidates = []
        while True:
            if nx<1 or nx>N or ny<1 or ny>N:
                break
            if board[nx][ny] == 0:
                break
            if board[nx][ny] == color:
                for xx, yy in candidates:
                    board[xx][yy] = color
                break
            candidates.append((nx, ny))
            nx, ny = nx+dx, ny+dy
            
TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    #black : 1, white : 2, none : 0
    board = [[0]*(N+1) for _ in range(N+1)]
    board[N//2][N//2] = 2
    board[N//2+1][N//2+1] = 2
    board[N//2][N//2+1] = 1
    board[N//2+1][N//2] = 1
    for _ in range(M):
        x, y, color = map(int, input().split())
        put(x, y, color)
    
    black = 0
    white = 0
    for x in range(1,N+1):
        for y in range(1, N+1):
            if board[x][y] == 1:
                black += 1
            elif board[x][y] == 2:
                white += 1
    
    print(f'#{tc} {black} {white}')
