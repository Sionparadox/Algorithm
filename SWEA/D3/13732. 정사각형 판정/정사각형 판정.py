def check(r, c):
    L = 0
    for i in range(c, N):
        if board[r][i] == '.':
            break
        L += 1
    if c+L > N:
        return False
    
    for i in range(L):
        for j in range(L):
            visited[r+i][c+j] = True
            if board[r+i][c+j] != '#':
                return False
    return True
    
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    board = [input() for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    answer = False
    flag = False
    for k in range(N*N):
        r, c = divmod(k, N)
        if board[r][c] == '#' and not visited[r][c]:
            if flag:
                answer = False
                break
            flag = True
            if check(r, c):
                answer = True
            else:
                break

    print(f"#{tc} {'yes' if answer else 'no'}")