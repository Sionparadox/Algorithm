import sys
input = sys.stdin.readline

T = int(input())
arr = [int(input()) for _ in range(T)]
K = max(arr)

directions = [(1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1), (1, 0)]
hexagon = {}

counts = [0]*6
answer = [0]*(K+1)

idx = 1
x, y = 1, 1
hexagon[(x, y)] = 1
answer[1] = 1
counts[1] = 1
depth = 1

def set_resource(x, y, idx):
    
    near = set()
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if (nx, ny) in hexagon:
            near.add(hexagon[(nx, ny)])
    
    selected = -1
    min_cnt = 10000
    for i in range(1, 6):
        if i in near:
            continue
        if counts[i]<min_cnt:
            min_cnt = counts[i]
            selected = i
     
    hexagon[(x, y)] = selected
    counts[selected] += 1
    answer[idx] = selected
    
while idx<K:
    idx += 1
    x, y = x+directions[0][0], y+directions[0][1]
    
    set_resource(x, y, idx)
    
    for d in range(1,6):
        length = depth
        if d == 1:
            length -= 1
        
        dx, dy = directions[d]
        for _ in range(length):
            if idx >= K:
                break
            x, y = x+dx, y+dy
            idx += 1
            set_resource(x, y, idx)
    
    for _ in range(depth):
        if idx >= K:
            break
        dx, dy = directions[0]
        x, y = x+dx, y+dy
        idx += 1
        set_resource(x, y, idx)
    
    depth += 1

for n in arr:
    print(answer[n])

'''
axial coordinate로 육각형을 표현
depth = max(abs(q), abs(r), abs(q+r))

외곽 육각형(ring)의 수 : depth*6 (0:1)
순서 : d[0] 1번, d[1] depth-1번 d[2]~d[5]~d[0] depth번씩 움직임
'''