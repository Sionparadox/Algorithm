import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
horse_dirs = [(2, 1), (1, 2), (-1, 2), (2, -1), (-2, 1), (1, -2), (-1, -2), (-2, -1)]

answer = -1
queue = deque([(0, 0, 0, 0)])

visited = set()
visited.add((0, 0, 0))

while queue:
    r, c, cnt, h = queue.popleft()
    if r == H-1 and c == W-1:
        answer = cnt
        break
    
    if h<K:
        for dr, dc in horse_dirs:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=H or nc<0 or nc>=W:
                continue
            if (nr, nc, h+1) not in visited and board[nr][nc] == 0:
                visited.add((nr, nc, h+1))
                queue.append((nr, nc, cnt+1, h+1))
    
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if nr<0 or nr>=H or nc<0 or nc>=W:
            continue
        if (nr, nc, h) not in visited and board[nr][nc] == 0:
            visited.add((nr, nc, h))
            queue.append((nr, nc, cnt+1, h))

print(answer)

'''
BFS로 탐색
방문처리 시 말 이동 횟수도 같이 카운트
'''