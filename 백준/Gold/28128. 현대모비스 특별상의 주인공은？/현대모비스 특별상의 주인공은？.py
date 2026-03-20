import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().split()) for _ in range(N)]
prize = set()

def check(x, y):
    name = board[x][y]
    if name in prize:
        return False
    
    for dx, dy in [(0, 1), (1, 0), (0, 2), (2, 0)]:
        nx, ny = x+dx, y+dy
        if nx<N and ny<M and board[nx][ny] == name:
            return True

for r in range(N):
    for c in range(M):
        if check(r, c):
            prize.add(board[r][c])

if not prize:
    print('MANIPULATED')
for name in sorted(list(prize)):
    print(name)
        

'''
받을 수 있는 경우
1. 2*1로 붙어있는 경우
2. 1*3 양끝에 붙어있는 경우

'''
