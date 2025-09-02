import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

tree = [[0]*(N+1) for _ in range(N+1)]

def update(r, c, value):
    x = r
    while x <= N:
        y = c
        while y <= N:
            tree[x][y] += value
            y += y&-y
        x += x&-x

def query(r, c):
    res = 0
    x = r
    while x > 0:
        y = c
        while y > 0:
            res += tree[x][y]
            y -= y&-y
        x -= x&-x
    return res

def range_sum(r1, c1, r2, c2):
    return query(r2, c2) - query(r2, c1-1) - query(r1-1, c2) + query(r1-1, c1-1)


for i in range(N):
    for j in range(N):
        update(i+1, j+1, board[i][j])

for _ in range(M):
    cmd = list(map(int, input().split()))
    if cmd[0] == 0:
        _, r, c, value = cmd
        diff = value - board[r-1][c-1]
        board[r-1][c-1] = value
        update(r, c, diff)
    else:
        _, r1, c1, r2, c2 = cmd
        print(range_sum(r1, c1, r2, c2))
'''
2차원 세그먼트 트리 : 세그먼트 트리 각 노드에 새로운 세그먼트 트리가 있는 구조

'''