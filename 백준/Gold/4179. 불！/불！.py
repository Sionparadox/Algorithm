import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
maze = [list(input().strip()) for _ in range(R)]

directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

JQueue = deque()
visited = set()
FQueue = deque()

for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            JQueue.append((i, j))
            visited.add((i, j))
            maze[i][j] = '.'
        if maze[i][j] == 'F':
            FQueue.append((i, j))

time = 0
while JQueue:
    time += 1
    
    for _ in range(len(FQueue)):
        fr, fc = FQueue.popleft()
        for dr, dc in directions:
            nr, nc = fr+dr, fc+dc
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                continue
            if maze[nr][nc] == '#' or maze[nr][nc] == 'F':
                continue
            maze[nr][nc] = 'F'
            FQueue.append((nr, nc))
    
    for _ in range(len(JQueue)):
        
        r, c = JQueue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                print(time)
                exit(0)
            if (nr, nc) not in visited and maze[nr][nc] == '.':
                JQueue.append((nr, nc))
                visited.add((nr, nc))

print("IMPOSSIBLE")