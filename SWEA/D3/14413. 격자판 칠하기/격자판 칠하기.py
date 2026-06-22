TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    symbol = ['#', '.']
    init = False
    flag = True
    for r in range(N):
        for c in range(M):
            if board[r][c] != '?':
                b = (r+c)%2
                if init:
                    if board[r][c] != symbol[b]:
                        flag = False
                        break
                else:
                    init = True
                    if symbol[b] != board[r][c]:
                        symbol[0], symbol[1] = symbol[1], symbol[0]
        if not flag:
            break
    
    print(f"#{tc} {'possible' if flag else 'impossible'}")