import sys
import heapq
input = sys.stdin.readline

N = int(input())
room = [list(input().strip()) for _ in range(N)]
doors = []
mirrors = []
for r in range(N):
    for c in range(N):
        if room[r][c] == '#':
            doors.append((r, c))
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def reflect(d):
    if d in (0, 1):
        return (2, 3)
    return (0, 1)

def solve(s, e):
    pq = []
    visited = [[[False]*4 for _ in range(N)] for _ in range(N)]
    for d in range(4):
        heapq.heappush(pq, (0, s[0], s[1], d))
    
    while pq:
        cnt, r, c, d = heapq.heappop(pq)
        dr, dc = directions[d]
        nr, nc = r+dr, c+dc
        while 0<=nr<N and 0<=nc<N and room[nr][nc] != '*':
            if room[nr][nc] == '!' and not visited[nr][nc][d]:
                visited[nr][nc][d] = True
                for nd in reflect(d):
                    heapq.heappush(pq, (cnt+1, nr, nc, nd))
            if nr == e[0] and nc == e[1]:
                return cnt
            nr, nc = nr+dr, nc+dc
    
    return -1

answer = solve(*doors)   
print(answer)

'''
visited에 r,c + 방향까지 체크
'''