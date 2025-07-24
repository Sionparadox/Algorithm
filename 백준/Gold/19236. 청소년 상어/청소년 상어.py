import sys
import copy
input = sys.stdin.readline

def next_dir(r, c, d, space):
    for i in range(8):
        dr, dc = directions[(d+i)%8]
        nr, nc = r+dr, c+dc
        if nr<0 or nr>=4 or nc<0 or nc>=4:
            continue
        if space[nr][nc] == 0:
            continue
        return (d+i)%8

    return -1

def move(fish, space):
    for num in range(1, 17):
        (r, c), d = fish[num]
        if (r, c) == (-1, -1):
            continue
        nd = next_dir(r, c, d, space)
        if nd == -1:
            continue
        dr, dc = directions[nd]
        nr, nc = r+dr, c+dc
        
        next_fish = space[nr][nc]
        fish[num] = [(nr, nc), nd]
        space[r][c], space[nr][nc] = space[nr][nc], space[r][c]
        if next_fish != -1:
            fish[next_fish][0] = (r, c)

def backTrack(fish, space, val):
    global answer
    fish = copy.deepcopy(fish)
    space = copy.deepcopy(space)
    move(fish, space)
    
    (r, c), d = fish[0]
    flag = False
    dr, dc = directions[d]
    for i in range(1,4):
        nr, nc = r+dr*i, c+dc*i
        if 0<=nr<4 and 0<=nc<4 and space[nr][nc] >0:
            flag = True
            
            food = space[nr][nc]
            nd = fish[food][1]
            fish[0] = [(nr, nc), nd]
            fish[food][0] = (-1, -1)
            space[nr][nc] = 0
            space[r][c] = -1
            
            backTrack(fish, space, val+food)
            
            fish[0] = [(r, c), d]
            fish[food][0] = (nr, nc)
            space[nr][nc] = food
            space[r][c] = 0

    answer = max(val, answer)

directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
space = [[-1]*4 for _ in range(4)]
fish = [[(-1,-1),-1] for _ in range(17)]

for r in range(4):
    _input = list(map(int, input().split()))
    for c in range(4):
        space[r][c] = _input[c*2]
        fish[_input[c*2]] = [(r, c), _input[c*2+1]-1]

answer = space[0][0]
fish[0] = fish[answer][:]
fish[answer][0] = (-1, -1)
space[0][0] = 0

backTrack(fish, space, answer)
print(answer)
'''
fish에 물고기 정보 저장 (r, c, d)
fish[0]은 상어
space에 물고기 죽으면 -1넣기
죽은 물고기 = [(-1, -1), d]

'''