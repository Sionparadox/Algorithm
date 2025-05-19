import sys
import copy
input = sys.stdin.readline

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
cleaner = []
for i in range(R):
    if room[i][0] == -1:
        cleaner.append(i)
        cleaner.append(i+1)
        break

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def spread():
    temp = [[0]*C for _ in range(R)]
    
    for r in range(R):
        for c in range(C):
            if room[r][c] > 0:
                candidate = []
                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc
                    if 0<=nr<R and 0<=nc<C and room[nr][nc] != -1:
                        candidate.append((nr, nc))
                dust = room[r][c]
                leftDust = dust
                for nr, nc in candidate:
                    temp[nr][nc] += dust//5
                    leftDust -= dust//5
                temp[r][c] += leftDust
    temp[cleaner[0]][0] = -1
    temp[cleaner[1]][0] = -1
    return temp

def clean():
    top, bottom = cleaner
    
    for r in range(top-1, 0, -1):  
        room[r][0] = room[r-1][0]
    for c in range(C-1):
        room[0][c] = room[0][c+1]
    for r in range(top):
        room[r][C-1] = room[r+1][C-1]
    for c in range(C-1, 1, -1):
        room[top][c] = room[top][c-1]
    room[top][1] = 0
    
    for r in range(bottom+1, R-1):
        room[r][0] = room[r+1][0]
    for c in range(C-1):
        room[R-1][c] = room[R-1][c+1]
    for r in range(R-1, bottom, -1):
        room[r][C-1] = room[r-1][C-1]
    for c in range(C-1, 1, -1):
        room[bottom][c] = room[bottom][c-1]
    room[bottom][1] = 0

for t in range(T):
    room = spread()
    clean()
print(sum(sum(row) for row in room)+2)