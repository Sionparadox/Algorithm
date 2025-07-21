import sys
import bisect
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
N = int(input())
path = [[] for _ in range(C)]

def drop(r, c, idx):
    while True:
        path[idx].append((r, c))
        if r == R-1 or board[r+1][c] == 'X':
            break
        if board[r+1][c] == 'O':
            if c > 0 and board[r][c-1] == '.' and board[r+1][c-1] == '.':
                c -= 1
            elif c < C-1 and board[r][c+1] == '.' and board[r+1][c+1] == '.':
                c += 1
            else:
                break
        r += 1
    board[r][c] = 'O'
    
    
for _ in range(N):
    x = int(input())-1
    while path[x]:
        r, c = path[x][-1]
        if board[r][c] == '.':
            break
        path[x].pop()
    
    if path[x]:
        r, c = path[x].pop()
        drop(r, c, x)
    else:
        drop(0, x, x)
    
for row in board:
    print(''.join(row))

'''
같은 열에 대한 입력일 때 떨어지는 경로는 이전에 갔던 경로와 일치함. 
뒷부분만 바뀜.
경로를 열 별로 저장해두고 뒤부터 pop하며 다음 위치를 찾기?
'''