import sys
input = sys.stdin.readline

dice = list(map(int, input().split()))

next_cell = {x:[x+1] for x in range(20)}
next_cell[5].append(21)
next_cell[10].append(24)
next_cell[15].append(26)
for idx in (21,22,24,26,27,28,29,30):
    next_cell[idx] = [idx+1]
next_cell[23], next_cell[25], next_cell[31], next_cell[20] = [29], [29], [20], [-1]
next_cell[-1] = [-1]
score = {x:x*2 for x in range(21)}
score[21], score[22], score[23] = 13,16,19
score[24], score[25] = 22,24
score[26], score[27], score[28] = 28, 27, 26
score[29], score[30], score[31] = 25, 30, 35

visited = [False]*32

def move(idx, k, shortcut=0):
    if idx == -1:
        return -1
    if k == 1:
        return next_cell[idx][shortcut]
    return move(next_cell[idx][shortcut], k-1)

answer = 0
def backTrack(d, val, pos):
    global answer
    if d == 10:
        answer = max(answer, val)
        return
    
    dist = dice[d]
    for mipple in range(4):
        idx = pos[mipple]
        if idx == -1:
            continue
        
        sc = 1 if idx in (5,10,15) else 0
        next_idx = move(idx, dist, sc)
        
        if next_idx == -1:
            visited[idx] = False
            pos[mipple] = next_idx
            backTrack(d+1, val, pos)
            pos[mipple] = idx
            visited[idx] = True
            
        elif not visited[next_idx]:
            visited[idx] = False
            visited[next_idx] = True
            pos[mipple] = next_idx
            backTrack(d+1, val+score[next_idx], pos)
            visited[idx] = True
            visited[next_idx] = False
            pos[mipple] = idx
    
backTrack(0, 0, [0,0,0,0])
print(answer)