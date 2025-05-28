import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
board = [[-1]*(C+1) for _ in range(R+1)]
directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
died = set()
sharks = []
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append((r, c, s, d-1, z))
    board[r][c] = i

def move (idx):
    r, c, s, d ,z = sharks[idx]
    board[r][c] = -1
    if d <= 1:
        s %= (R-1)*2
    else :
        s %= (C-1)*2
    leftMove = s
    while leftMove>0:
        dr, dc = directions[d]
        if r+dr == 0 or c+dc == 0 or r+dr>R or c+dc>C:
            if d %2 == 0:
                d += 1
            else :
                d -= 1
            dr, dc = directions[d]
        r += dr
        c += dc
        leftMove -= 1
    sharks[idx] = (r, c, s, d, z)

answer = 0
for c in range(1, C+1):
    for r in range(1, R+1):
        cell = board[r][c]
        if cell != -1:
            died.add(cell)
            answer += sharks[cell][4]
            board[r][c] = -1
            break
    
    for i in range(M):
        if i not in died:
            move(i)
    for i in range(M):
        if i not in died:
            sr, sc, s, d, z = sharks[i]
            cell = board[sr][sc]
            if cell == -1:
                board[sr][sc] = i
            elif sharks[cell][4] > z:
                died.add(i)
            else :
                board[sr][sc] = i
                died.add(cell)
                
print(answer)

'''
일단 왼쪽, 위에 1칸씩 padding
빈칸은 -1
상어가 있는곳은 상어의 인덱스보관
sharks 에는 속도, 방향, 크기 를 넣어둠 (상어정보) << 움직임 이후에는 갱신.

'''
