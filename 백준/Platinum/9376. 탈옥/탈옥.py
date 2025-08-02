import sys
from collections import deque
input = sys.stdin.readline

def BFS(r, c, board):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    R = len(board)
    C = len(board[0])
    res = [[float('inf')]*C for _ in range(R)]
    res[r][c] = 0
    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            nxt = res[r][c]
            if nr<0 or nr>=R or nc<0 or nc>=C:
                continue
            if board[nr][nc] == '*':
                continue
            if board[nr][nc] == '#':
                nxt += 1
            if res[nr][nc] > nxt:
                res[nr][nc] = nxt
                queue.append((nr, nc))
    
    return res
    
def solve(R, C, board):
    pos = [(0, 0)]
    for r in range(1, R-1):
        for c in range(1, C-1):
            if board[r][c] == '$':
                pos.append((r, c))
    cnt = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] == '#':
                cnt[r][c] = -2
    
    for r, c in pos:
        tmp = BFS(r, c, board)
        for i in range(R):
            for j in range(C):
                cnt[i][j] += tmp[i][j]
    return min(min(row) for row in cnt)

T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    arr = [['.']*(C+2)]+[['.']+list(input().strip())+['.'] for _ in range(R)]+[['.']*(C+2)]
    print(solve(R+2, C+2, arr))

'''
벽 바깥에 '.'로 한칸씩 패딩
0,0과 죄수의 좌표 2곳에서 모든 칸까지의 지나온 문의 수를 계산. 
이후 3값의 합이 최소인 칸을 지나는 경로가 답
값에서 벽인 칸은 2씩 빼야함
'''