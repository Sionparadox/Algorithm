import sys
from itertools import combinations
input = sys.stdin.readline

N, M, H = map(int, input().split())
ladder = [[0]*N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1
    
possible = []
for i in range(H):
    for j in range(N - 1):
        if ladder[i][j]: continue
        if j > 0 and ladder[i][j-1]: continue
        if j < N - 2 and ladder[i][j+1]: continue
        possible.append((i, j))

def check():
    for c in range(N):
        now = c
        for r in range(H):
            if ladder[r][now]:
                now += 1
            elif now > 0 and ladder[r][now-1]:
                now -= 1
        if now != c:
            return False
    return True

def validation(positions):
    for (r, c) in positions:
        if ladder[r][c]: return False
        if c > 0 and ladder[r][c-1]: return False
        if c < N-2 and ladder[r][c+1]: return False
    
    for (r, c) in positions:
        ladder[r][c] = 1

    if check():
        return True
        
    for (r, c) in positions:
        ladder[r][c] = 0
    return False

answer = -1
for k in range(M % 2, 4, 2):
    for positions in combinations(possible, k):
        if validation(positions):
            answer = k
            break
    if answer != -1:
        break        
        
print(answer)

'''
가로선 시작 부분에 방문체크
백트래킹으로 체크하면서 반환
'''