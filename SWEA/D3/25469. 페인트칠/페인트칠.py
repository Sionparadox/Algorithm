TC = int(input())
for _ in range(TC):
    H, W = map(int, input().split())
    board = [input() for _ in range(H)]
    rows = cols = 0
    
    for r in range(H):
        if all(board[r][c] == '#' for c in range(W)):
            rows += 1
    for c in range(W):
        if all(board[r][c] == '#' for r in range(H)):
            cols += 1
    
    if rows == H and cols == W:
        print(min(H, W))
    else:
        print(rows+cols)