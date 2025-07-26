import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dirMapper = {1:3, 2:1, 3:0, 4:2}
answer = [0]*4
line = [0]*(N**2)

r = c = N//2
dir = 0
idx = 0
for i in range(1, N+1):
    for _ in range(2):
        dr, dc = directions[dir]
        for _ in range(i):
            if idx==N**2: break
            line[idx] = board[r][c]
            idx += 1
            r, c = r+dr, c+dc
        dir = (dir+1)%4 

LDRU = []
i = 1
increase = 2
while i<N**2:
    for _ in range(4):
        LDRU.append(i)
        i += increase
    i += 1
    increase += 2

def blizzard(d, s):
    for i in range(s):
        n = LDRU[d+i*4]
        line[n] = 0

def arrange(line):
    res = [0]
    for i in range(N**2):
        if line[i] != 0:
            res.append(line[i])
    return res + [0]*(N**2-len(res))

def explode(line):
    isExplode = True
    while isExplode:
        isExplode = False
        line = arrange(line)
        prev = line[1]
        cnt = 0
        for i in range(1, N**2):
            now = line[i]
            if prev == now:
                cnt += 1
            else:
                if cnt >=4:
                    isExplode = True
                    for k in range(1, cnt+1):
                        line[i-k] = 0
                    answer[prev] += cnt
                prev = now
                cnt = 1
                    
    
    return line

def change(line):
    res = [0]
    idx = 1
    cnt = 0
    prev = line[1]
    while idx<N**2:
        now = line[idx]
        if now == prev:
            cnt += 1
        else:
            res.append(cnt)
            res.append(prev)
            cnt = 1
            prev = now
        idx += 1

    if len(res) >=N**2:
        return res[:N**2]
    else:
        return res+[0]*(N**2-len(res))


for _ in range(M):
    d, s = map(int, input().split())
    d = dirMapper[d]
    blizzard(d, s)
    line = explode(line)
    line = change(line)

print(sum([x*answer[x] for x in range(4)]))