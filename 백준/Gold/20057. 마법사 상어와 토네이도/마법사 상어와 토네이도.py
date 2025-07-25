import sys
input = sys.stdin.readline

N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] #LDRU

def pattern(d):
    dr, dc = directions[d]
    return [
        (dr*2, dc*2, 0.05),
        (dr-dc, dc-dr, 0.1),
        (dr+dc, dc+dr, 0.1),
        (-dc, -dr, 0.07),
        (dc, dr, 0.07),
        (-dc*2, -dr*2, 0.02),
        (dc*2, dr*2, 0.02),
        (-dr-dc, -dc-dr, 0.01),
        (-dr+dc, -dc+dr, 0.01),
        (dr, dc, 0)
    ]

def spread(r, c, d):
    outs = 0
    tot = sand[r][c]
    for dr, dc, val in pattern(d):
        nr, nc = r+dr, c+dc
        moved = int(tot*val)
        if val == 0:
            moved = sand[r][c]
        if nr<0 or nr>=N or nc<0 or nc>=N:
            outs += moved
        else:
            sand[nr][nc] += moved
        sand[r][c] -= moved

    return outs

answer = 0
r = c = N//2
d = 0
for i in range(1,N+1):
    for _ in range(2):
        for k in range(i):
            if (r, c) == (0, 0):
                break
            dr, dc = directions[d]
            r, c = r+dr, c+dc
            answer += spread(r, c, d)
            
        d = (d+1)%4
print(answer)
'''
5%  r+dr*2, c+dc*2
10% r+dr+-abs(dc), c+dc+-abs(dr)
7%  r+-abs(dc), c+-abs(dr)
2%  r+-abs(dc*2), c+-abs(dr*2)
1%  r-dr+-abs(dc), c-dc+-abs(dr)
'''
    