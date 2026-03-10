import sys
from collections import deque
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

queue = deque(start)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0
cnt = K
while queue:
    answer += 1
    for _ in range(len(queue)):
        r, c = queue.popleft()
        civil = lands[r][c]
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            target = lands[nr][nc]
            if target == civil:
                continue
            if target == -1:
                lands[nr][nc] = civil
                queue.append((nr, nc))
            
            elif target < civil:
                if union(target, civil):
                    cnt -= 1
                    if cnt == 1:
                        print(answer)
                        exit(0)
            
            else:
                if union(target, civil):
                    cnt -= 1
                    if cnt == 1:
                        print(answer-1)
                        exit(0)
                    

'''
Leveling BFS로 문명 확장
이후 분리집합으로 문명 합치기
-> 문명이 올해 확장해서 겹쳐서 만난건지 딱 만난건지 확인 필요
queue에 항상 더 작은 번호의 문명이 먼저 들어가므로 확장할때 번호 대소관계로 유추 가능
- 확장한 땅이 더 작은 마킹이 있으면 이번턴에 겹치게 만난것
- 확장한 땅에 더 큰 마킹이 있으면 전턴에 딱 만났었다는 것
'''