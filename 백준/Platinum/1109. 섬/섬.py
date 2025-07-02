import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]
board = [[0]*(M+2)]
for line in arr:
    temp = [0]
    for c in line:
        if c == 'x':
           temp.append(1) 
        else:
            temp.append(0)
    temp.append(0)
    board.append(temp)
board += [[0]*(M+2)]

visited = [[False]*(M+2) for _ in range(N+2)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
def BFS(r, c):
    queue = deque([(r, c)])
    res = set()
    k = board[r][c]
    d = 4*(k+1)
    visited[r][c] = True
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions[:d]:
            nr, nc = r+dr, c+dc
            if nr < 0 or nr > N+1 or nc < 0 or nc > M+1:
                continue
            
            if not visited[nr][nc]:
                if board[nr][nc] == k:
                    queue.append((nr, nc))
                    visited[nr][nc] = True
                else:
                    res.add((nr, nc))
    return res

answer = [0]*(min(N, M)+1)
def DFS(ocean):
    islands = set()
    height = 0
    for r, c in ocean:
        if not visited[r][c]:
            islands.update(BFS(r, c))
    
    for r, c in islands:
        if not visited[r][c]:
            height = max(height, DFS(BFS(r, c))+1)
    
    answer[height] += 1
    return height

DFS([(0,0)])
while answer.pop() == 0:
    continue
if not answer:
    print(-1)
else:
    print(' '.join(map(str, answer)))
'''
바다 -> 0 땅 -> 1
지도에 4방향에 0으로 1씩 패딩을 줘서 바다가 모든 땅을 포함하도록 변경
DFS로 0,0부터 시작
육지를 만나면 BFS로 연결된 육지와 연결된 바다를 반환
바다 BFS는 4방향, 육지 BFS는 8방향

'''
