import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
move = [x-1 for x in map(int, list(input().strip()))]

directions = [[1, -1], [1, 0], [1, 1], [0, -1], [0, 0], [0, 1], [-1, -1], [-1, 0], [-1, 1]]

pos = (-1, -1)
enemy = []
for i in range(R):
    for j in range(C):
        if board[i][j] == 'I':
            pos = (i, j)
        if board[i][j] == 'R':
            enemy.append((i, j))

for i in range(len(move)):
    dr, dc = directions[move[i]]
    r, c = pos[0]+dr, pos[1]+dc
    pos = (r, c)
    visited = set()
    explode = set()
    
    for tr, tc in enemy:
        if tr == r and tc == c:
            print("kraj",i+1)
            exit(0)
        dr = dc = 0
        if r != tr:
            dr = (r-tr)//abs(r-tr)
        if c != tc:
            dc = (c-tc)//abs(c-tc)
        nr, nc = tr+dr, tc+dc
        if nr == r and nc == c:
            print("kraj",i+1)
            exit(0)
        if (nr, nc) in explode:
            continue
        elif (nr, nc) in visited:
            explode.add((nr, nc))
            visited.remove((nr, nc))
        else:
            visited.add((nr, nc))
        
    enemy = list(visited)

board = [['.']*C for _ in range(R)]
board[pos[0]][pos[1]] = 'I'
for tr, tc in enemy:
    board[tr][tc] = 'R'

for row in board:
    print(''.join(row))
'''
me : 4,4
e : (3, 0), (2, 9)
d : (1, 1), (1, -1)
'''
