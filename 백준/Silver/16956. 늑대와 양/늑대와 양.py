import sys
input = sys.stdin.readline

R, C = map(int, input().split())
pasture = [list(input().strip()) for _ in range(R)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for r in range(R):
    for c in range(C):
        if pasture[r][c] == 'S':
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr<0 or nr>=R or nc<0 or nc>=C:
                    continue
                if pasture[nr][nc] == '.':
                    pasture[nr][nc] = 'D'
                elif pasture[nr][nc] == 'W':
                    print(0)
                    exit(0)

print(1)
print('\n'.join(''.join(row) for row in pasture))