def check(symbol):
    for r in range(4):
        if all(board[r][c] in (symbol, 'T') for c in range(4)):
            return True
    for c in range(4):
        if all(board[r][c] in (symbol, 'T') for r in range(4)):
            return True
    if all(board[i][i] in (symbol, 'T') for i in range(4)):
        return True
    if all(board[3-i][i] in (symbol, 'T') for i in range(4)):
        return True
    return False

TC = int(input())
for tc in range(1, TC+1):
    board = [input() for _ in range(4)]
    is_full = True
    for r in range(4):
        for c in range(4):
            if board[r][c] == '.':
                is_full = False
                break
        if not is_full:
            break
    
    if check('X'):
        answer = 'X won'
    elif check('O'):
        answer = 'O won'
    elif is_full:
        answer = 'Draw'
    else:
        answer = 'Game has not completed'
    
    print(f'#{tc} {answer}')
    if tc != TC:
        input()