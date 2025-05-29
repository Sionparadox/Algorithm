N, M = map(int, input().split())
board = [['#'] * (M + 2)] + [['#'] + list(input().strip()) + ['#'] for _ in range(N)] + [['#'] * (M + 2)]

def shoot(i, j):
    visited = set()
    if i == 0:
        di, dj = 1, 0
    elif i == N + 1:
        di, dj = -1, 0
    elif j == 0:
        di, dj = 0, 1
    elif j == M + 1:
        di, dj = 0, -1
    
    res = 0
    while 1:
        if (i, j, di, dj) in visited:
            return False
        visited.add((i, j, di, dj))
        i += di
        j += dj
        if board[i][j] == '#':
            break
        if board[i][j] == '/':
            di, dj = -dj, -di
        elif board[i][j] == '\\':
            di, dj = dj, di
        res += 1
    return res
answer = 0
for i in (0, N + 1):
    for j in range(1, M+1):
        res = shoot(i, j)
        if res == -1:
            print(-1)
            exit()
        answer = max(answer, res)
for j in (0, M + 1):
    for i in range(1, N + 1):
        res = shoot(i, j)
        if res == -1:
            print(-1)
            exit()
        answer = max(answer, res)
print(answer)
