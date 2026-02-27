import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
indexed = [[0]*N for _ in range(N)]

def find_land(r, c, k):
    queue = deque([(r, c)])
    edge = set()
    indexed[r][c] = k
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if indexed[nr][nc] > 0:
                continue
            if board[nr][nc]:
                indexed[nr][nc] = k
                queue.append((nr, nc))
            else:
                edge.add((r, c))
    
    return edge

cnt = 1
edges = []
for r in range(N):
    for c in range(N):
        if board[r][c] and indexed[r][c] == 0:
            edges.extend(find_land(r, c, cnt))
            cnt += 1

answer = 0
queue = deque(edges)
sign = 1
while True:
    answer += 1
    sign *= -1
    for _ in range(len(queue)):
        r, c = queue.popleft()
        k = abs(indexed[r][c])
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if abs(indexed[nr][nc]) == k:
                continue
            if indexed[nr][nc] == 0:
                indexed[nr][nc] = k*sign
                queue.append((nr, nc))
            else:
                if indexed[nr][nc]*sign > 0:
                    answer = 2*answer -1
                else:
                    answer = (answer-1)*2
                print(answer)
                exit(0)
    
'''
BFS로 육지를 탐색
육지를 인덱싱(1-based)해두고 해변 타일을 저장해둠
이후 해변 타일에 대해 바다를 향해 leveling BFS
모든 섬이 동일한 거리로 확장하며 지나온 길은 짝수턴, 홀수턴에 따라 부호를 바꿔가며 저장
BFS를 돌다 동일한 점에 도착하면 부호에 따라 이번턴에 동시에 만난건지, 지난턴에 밟아둔건지 판정
'''