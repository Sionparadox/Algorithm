import sys
from collections import deque
input = sys.stdin.readline

N, M, K, T = map(int, input().split())
start = [tuple(map(int, input().split())) for _ in range(M)]
area = [tuple(map(int, input().split())) for _ in range(K)]

visited = [[[-1]*2 for _ in range(N+1)] for _ in range(N+1)]
directions = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]

queue = deque()
for r, c in start:
    queue.append((r, c, 0))

while queue:
    r, c, t = queue.popleft()
    if t == T:
        continue
    p = (t+1)%2
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if nr<=0 or nr>N or nc<=0 or nc>N:
            continue
        if visited[nr][nc][p] == -1:
            visited[nr][nc][p] = t+1
            queue.append((nr, nc, t+1))


flag = False
p = T%2
for r, c in area:
    if visited[r][c][p] != -1:
        flag = True
        break

print("YES" if flag else "NO")

'''
BFS? 9만 * 만 -> 시간초과
1) 중앙칸은 0,2일차에 더러움.
 + 1일차에 더러운칸은 3일차에도 더러움

2) 중앙칸은 계속 더러움
 + 1일차에 더러운 칸은 그 이후에도 계속 더러움

-> 한번 방문한 이후에는 같은 홀/짝에 대해 같은 값 유지.
-> 홀수일때 방문 : 그 이후 홀수 다 방문됨
-> 짝수일때도 방문 : 그 이후 짝수 다 방문됨
visited[r][c][p] : r행, c열, p(홀/짝)로 방문

visited[r][c][0] << 초기화x
-> 1x1 (1,1) 같은 곰팡이가 번식 못하고 사라지는 반례 존재
'''
    
