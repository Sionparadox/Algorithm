import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
lake = [list(input().strip()) for _ in range(R)]
melt_day = [[-1]*C for _ in range(R)]
pos = []
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

queue = deque()
for r in range(R):
    for c in range(C):
        if lake[r][c] == 'L':
            pos.append((r, c))
        if lake[r][c] != 'X':
            melt_day[r][c] = 0
            queue.append((r, c))

maxDay = -1
while queue:
    r, c = queue.popleft()
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if nr<0 or nr>=R or nc<0 or nc>=C:
            continue
        if melt_day[nr][nc] != -1:
            continue
        if lake[nr][nc] == 'X':
            melt_day[nr][nc] = melt_day[r][c] + 1
            maxDay = melt_day[nr][nc]
            queue.append((nr, nc))


def check(k):
    queue = deque([pos[0]])
    visited = [[False]*C for _ in range(R)]
    visited[pos[0][0]][pos[0][1]] = True
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=R or nc<0 or nc>=C:
                continue
            if (nr, nc) == pos[1]:
                return True
            if visited[nr][nc] or melt_day[nr][nc]>k:
                continue
            visited[nr][nc] = True
            queue.append((nr, nc))
    
    return False

s = 0
e = maxDay

while s<e:
    mid = (s+e)//2
    if check(mid):
        e = mid
    else:
        s = mid+1

print(s)

'''
빙판이 녹는 날짜를 만들고
K에 대해 이분탐색하며 연결되었는지 확인
'''