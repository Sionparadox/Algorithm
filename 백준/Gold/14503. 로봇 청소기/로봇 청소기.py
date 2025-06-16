import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

answer = 0
while True:
    if not visited[r][c] and room[r][c] == 0:
        answer += 1
        visited[r][c] = True
    needClean = False
    for dr, dc in direction:
        nr, nc = r+dr, c+dc
        if not visited[nr][nc] and room[nr][nc] == 0:
            needClean = True
            break
    if not needClean:
        dr, dc = direction[d]
        r, c = r-dr, c-dc
        if room[r][c] == 1:
            break
    else:
        while True:
            d = (d-1)%4
            dr, dc = direction[d]
            nr, nc = r+dr, c+dc
            if room[nr][nc] == 0 and not visited[nr][nc]:
                r, c = nr, nc
                break

print(answer)

        