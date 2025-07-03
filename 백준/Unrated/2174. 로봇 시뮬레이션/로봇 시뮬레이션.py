import sys
input = sys.stdin.readline

C, R = map(int, input().split())
N, M = map(int, input().split())
board = [[0]*C for _ in range(R)]
robots = [(-1, -1, -1)]*(N+1)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] #URDL
mapper = {'N':2, 'S':0, 'E':1, 'W':3}

for idx in range(1, N+1):
    c, r, d = input().split()
    r, c = int(r)-1, int(c)-1
    robots[idx] = (r, c, mapper[d])
    board[r][c] = idx

def practice(idx, k, cmd):
    r, c, d = robots[idx]
    if cmd == 'F':
        dr, dc = directions[d]
        nr, nc = r, c
        for _ in range(k):
            nr, nc = nr+dr, nc+dc
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                print(f'Robot {idx} crashes into the wall')
                return False
            if board[nr][nc] != 0:
                print(f'Robot {idx} crashes into robot {board[nr][nc]}')
                return False
        board[r][c] = 0
        board[nr][nc] = idx
        robots[idx] = (nr, nc, d)
    else:
        d = (d+k)%4 if cmd == 'L' else (d-k)%4
        robots[idx] = (r, c, d)
    return True

for _ in range(M):
    idx, cmd, k = input().split()
    if not practice(int(idx), int(k), cmd):
        exit(0)

print('OK')  