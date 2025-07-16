import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[0]*M for _ in range(N)]

def canPlace(r, c, arr):
    H = len(arr)
    W = len(arr[0])
    if N-r < H or M-c < W :
        return False
    for i in range(H):
        for j in range(W):
            if arr[i][j] and board[i+r][j+c]:
                return False
    return True

def place(arr):
    H = len(arr)
    W = len(arr[0])
    for i in range(N):
        for j in range(M):
            flag = canPlace(i, j, arr)
            if flag:
                for x in range(H):
                    for y in range(W):
                        board[i+x][j+y] = arr[x][y] | board[i+x][j+y]
                return True
    return False

def rotate(arr):
    return [list(row) for row in zip(*reversed(arr))]

for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    for _ in range(4):
        flag = place(sticker)
        if flag:
            break
        sticker = rotate(sticker)
        R, C = C, R

print(sum(sum(row) for row in board))