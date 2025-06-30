import sys
input = sys.stdin.readline

L = int(input())
N = int(input())
if N == 0:
    print(L+1)
    exit(0)
command = []
for _ in range(N):
    t, d = input().strip().split(' ')
    t = int(t)
    command.append((t, d))
command.append((2*L+1, 0))

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)] #RDLU
def rotate(d, r):
     return (d+1)%4 if r == 'R' else (d-1)%4

lines = [(L+1, L+1, L+1, -L), (L+1, -L-1, -L, -L-1), (-L-1, -L-1, -L-1, L), (-L-1, L+1, L, L+1)]

def intersection(x1, y1, x2, y2):
    minDist = float('inf')
    for a1, b1, a2, b2 in lines:
        # 선분이 수직
        if x1 == x2:
            # 비교군이 수직
            if a1 == a2:
                if x1 == a1:
                    y_overlap_start = max(min(y1, y2), min(b1, b2))
                    y_overlap_end = min(max(y1, y2), max(b1, b2))
                    if y_overlap_start <= y_overlap_end:
                        dist1 = abs(y_overlap_start - y1)
                        dist2 = abs(y_overlap_end - y1)
                        minDist = min(minDist, dist1, dist2)
            else:
                # 비교군이 수평
                # 내 x좌표가 비교선분 x구간에 포함, 비교 y좌표가 내 y구간에 포함
                if min(a1, a2) <= x1 <= max(a1, a2) and min(y1, y2) <= b1 <= max(y1, y2):
                    dist = abs(x1 - x1) + abs(b1 - y1)
                    minDist = min(minDist, dist)
        else:
            # 선분이 수평
            if b1 == b2:
                # 비교군이 수평
                if y1 == b1:
                    x_overlap_start = max(min(x1, x2), min(a1, a2))
                    x_overlap_end = min(max(x1, x2), max(a1, a2))
                    if x_overlap_start <= x_overlap_end:
                        dist1 = abs(x_overlap_start - x1)
                        dist2 = abs(x_overlap_end - x1)
                        minDist = min(minDist, dist1, dist2)
            else:
                # 비교군이 수직
                if min(x1, x2) <= a1 <= max(x1, x2) and min(b1, b2) <= y1 <= max(b1, b2):
                    dist = abs(a1 - x1) + abs(y1 - y1)
                    minDist = min(minDist, dist)
    return minDist

pos = (0, 0)
dir = 0
time = 0
for t, r in command:
    x, y = pos
    dx, dy = directions[dir]
    nx, ny = x+dx*t, y+dy*t
    dist = intersection(x,y,nx,ny)
    if dist == float('inf'):
        lines.append((x, y, nx-dx, ny-dy))
        dir = rotate(dir, r)
    else:
        time += dist
        break
    
    time += t
    pos = (nx, ny)

print(time)
    

'''
L이 최대 1억이라 visited 2차원 배열은 불가능, set도 최악의 경우에서 불가능
뱀의 방문 경로를 선분으로 저장해서 새로운 이동마다 선분과 겹치는지 확인
선분 최대 N개 -> 매번 N 개에 대해 검사하므로 O(N^2) -> 1000^2
line[i] = (x1, y1, x2, y2)
꺾이는 부분은 다음 선분의 시작점. 이번 선분은 꺾이기 전 점까지
'''