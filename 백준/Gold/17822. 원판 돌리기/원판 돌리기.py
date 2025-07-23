import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
circle = [list(map(int, input().split())) for _ in range(N)]

def spin(idx, d, k):
    if d == 0:
        k = M-k
    
    circle[idx] = circle[idx][k:] + circle[idx][:k]

def adjust():
    duplicate = set()
    tot = 0
    cnt = 0
    for i in range(N):
        for j in range(M):
            tot += circle[i][j]
            if circle[i][j] == 0:
                continue
            
            cnt += 1
            if circle[i][j] == circle[i][(j-1)%M]:
                duplicate.add((i, j))
                duplicate.add((i, (j-1)%M))
            if circle[i][j] == circle[i][(j+1)%M]:
                duplicate.add((i, j))
                duplicate.add((i, (j+1)%M))
            if i>0 and circle[i][j] == circle[i-1][j]:
                duplicate.add((i, j))
                duplicate.add((i-1, j))
            if i<N-1 and circle[i][j] == circle[i+1][j]:
                duplicate.add((i, j))
                duplicate.add((i+1, j))
    
    if cnt == 0:
        return
    
    for r, c in duplicate:
        circle[r][c] = 0
        
    if len(duplicate) == 0:
        avg = tot/cnt
        for i in range(N):
            for j in range(M):
                if circle[i][j] == 0:
                    continue
                if circle[i][j] > avg:
                    circle[i][j] -= 1
                elif circle[i][j] < avg:
                    circle[i][j] += 1
                
for _ in range(T):
    x, d, k = map(int, input().split())
    
    for i in range(x, N+1, x):
        spin(i-1, d, k)
    adjust()
print(sum(sum(row) for row in circle))
