import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS():
    fire = deque()
    queue = deque()
    for r in range(H):
        for c in range(W):
            if building[r][c] == '@':
                queue.append((r, c))
                visited[r][c] = True
            if building[r][c] == '*':
                fire.append((r, c))
                visited[r][c] = True

    move = 0
    while queue:
        move += 1
        for  _ in range(len(fire)):
            r, c = fire.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr<0 or nr>=H or nc<0 or nc>=W:
                    continue
                if visited[nr][nc] or building[nr][nc] == '#':
                    continue
                visited[nr][nc] = True
                fire.append((nr, nc))
                   
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr<0 or nr>=H or nc<0 or nc>=W:
                    return move
                if visited[nr][nc] or building[nr][nc] != '.':
                    continue
                visited[nr][nc] = True
                queue.append((nr, nc))
                
    return "IMPOSSIBLE"

for _ in range(T):
    W, H = map(int, input().split())
    building = [list(input().rstrip()) for _ in range(H)]
    visited = [[False]*W for _ in range(H)]
    print(BFS())
    
            
 
'''
불, 사람 위치를 동시에 leveling BFS
불 확장이 먼저, 이후 사람 이동

visited 공유 가능? yes
-> 사람이 있는곳에 불이 확장하지 못함. 
-> But, 확장하지 않더라도 그 위치로 확장하는건 결과에 영향X(불이 뒤쫓아가는 모습)
'''