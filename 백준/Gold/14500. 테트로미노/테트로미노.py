import sys
input = sys.stdin.readline

tetromino = [[(0,1),(0,2),(0,3)], [(1,0),(2,0),(3,0)],[(0,1),(1,0),(1,1)],[(0,1),(1,1),(1,2)],[(0,1),(-1,1),(-1,2)],[(1,0),(1,1),(2,1)],[(-1,0),(-1,1),(-2,1)],[(0,1),(1,1),(0,2)],[(0,1),(-1,1),(0,2)],[(1,0),(1,1),(2,0)],[(0,1),(-1,1),(1,1)],[(1,0),(2,0),(2,1)],[(0,1),(-1,1),(-2,1)],[(1,0),(0,1),(0,2)],[(0,1),(0,2),(1,2)],[(0,1),(1,1),(2,1)],[(0,1),(1,0),(2,0)],[(0,1),(0,2),(-1,2)],[(1,0),(1,1),(1,2)]]


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def TetSum(r, c, idx):
    tet = tetromino[idx]
    res = board[r][c]
    for dr, dc in tet:
        nr = r+dr
        nc = c+dc
        if nr<0 or nr>=N or nc<0 or nc>=M:
            return 0
        res += board[nr][nc]
    return res

answer = 0
for r in range(N):
    for c in range(M):
        for i in range(19):
            answer = max(answer, TetSum(r, c, i))

print(answer)

'''
미리 테트로미노 배열로 모든 모양을 저장해둔다?
I : 2
O : 1
S : 4
T : 4
L : 8
총 19개
'''