import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().split())
parent = [x for x in range(K)]
start = []
lands = [[-1]*N for _ in range(N)]
for i in range(K):
    r, c = map(int, input().split())
    start.append((r-1, c-1))
    lands[r-1][c-1] = i

def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    u, v = find(u), find(v)
    if u == v:
        return False
    
    parent[v] = u
    return True

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = deque(start)

cnt = 0

def check(r, c):
    curr = lands[r][c]
    res = 0
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if nr<0 or nr>=N or nc<0 or nc>=N:
            continue
        if lands[nr][nc] != -1 and lands[nr][nc] != curr:
            if union(curr, lands[nr][nc]):
                res += 1
    return res

for r, c in start:
    cnt += check(r, c)

if cnt == K-1:
    print(0)
    exit(0)

answer = 0
while queue:
    answer += 1
    for _ in range(len(queue)):
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if lands[nr][nc] == -1:
                lands[nr][nc] = lands[r][c]
                queue.append((nr, nc))
                cnt += check(nr, nc)
                if cnt == K-1:
                    print(answer)
                    exit(0)
                


'''
Leveling BFS로 문명 확장
확장한 위치 주변에 다른 문명이 있는지 검사
'''