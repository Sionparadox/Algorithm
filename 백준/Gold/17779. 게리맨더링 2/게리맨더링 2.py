import sys
input = sys.stdin.readline

N = int(input())
population = [list(map(int, input().split())) for _ in range(N)]

def calc(x, y, d1, d2):
    cnt = [0]*5
    for r in range(N):
        for c in range(N):
            if r < x+d1 and c<=y and r+c < x+y:
                cnt[0] += population[r][c]
            elif r<=x+d2 and c>y and c-r > y-x:
                cnt[1] += population[r][c]
            elif c>=y-d1+d2 and r+c > x+y+d2*2:
                cnt[2] += population[r][c]
            elif r-c > x-y+d1*2:
                cnt[3] += population[r][c]
            else:
                cnt[4] += population[r][c]
    
    return max(cnt) - min(cnt)

answer = float('inf')
for r in range(N):
    for c in range(N):
        if r in (0, N-1) and c in (0, N-1):
            continue
        
        for d1 in range(1, min(c+1, N-r)):
            for d2 in range(1, min(N-c, N-r+d1)):
                answer = min(answer, calc(r, c, d1, d2))

print(answer)