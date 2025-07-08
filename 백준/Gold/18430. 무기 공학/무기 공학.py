import sys
input = sys.stdin.readline

N, M = map(int, input().split())
woods = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] #URDL
answer = 0

def check(r, c, d):
    dr, dc = directions[d]
    r, c = r+dr, c+dc
    if r<0 or r>=N or c<0 or c>=M:
        return (-1, -1)
    if visited[r][c]:
        return(-1, -1)
    return (r, c)

def backTrack(pos, k):
    global answer
    if pos == N*M:
        answer = max(answer, k)
        return
    
    r, c = divmod(pos, M)
    if not visited[r][c]:
        for d in range(4):
            r1, c1 = check(r, c, d)
            r2, c2 = check(r, c, (d+1)%4)
            if r1 == -1 or r2 == -1:
                continue
            visited[r][c] = True
            visited[r1][c1] = True
            visited[r2][c2] = True
            nk = k+woods[r][c]*2+woods[r1][c1]+woods[r2][c2]
            backTrack(pos+1, nk)
            visited[r][c] = False
            visited[r1][c1] = False
            visited[r2][c2] = False
    
    backTrack(pos+1, k)

backTrack(0, 0)
print(answer)
            