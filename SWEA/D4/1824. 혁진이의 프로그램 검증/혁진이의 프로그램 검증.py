from collections import deque

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # LRUD

def solve():
    queue = deque([(0, 0, 1, 0)])

    while queue:
        r, c, d, memory = queue.popleft()

        if visited[r][c][memory][d]:
            continue
        visited[r][c][memory][d] = True

        ch = cmd[r][c]
        if ch == '@':
            return True

        if ch.isdigit():
            memory = int(ch)
        elif ch == '+':
            memory = (memory + 1) % 16
        elif ch == '-':
            memory = (memory - 1) % 16
        elif ch == '_':
            d = 0 if memory else 1
        elif ch == '|':
            d = 2 if memory else 3
        elif ch == '<':
            d = 0
        elif ch == '>':
            d = 1
        elif ch == '^':
            d = 2
        elif ch == 'v':
            d = 3
        elif ch == '?':
            for nd in range(4):
                nr = (r + directions[nd][0]) % R
                nc = (c + directions[nd][1]) % C
                queue.append((nr, nc, nd, memory))
            continue

        nr = (r + directions[d][0]) % R
        nc = (c + directions[d][1]) % C
        queue.append((nr, nc, d, memory))

    return False

TC = int(input())
for tc in range(1, TC+1):
    R, C = map(int, input().split())
    cmd = [input() for _ in range(R)]
    visited = [[[[False] * 4 for _ in range(16)] for _ in range(C)] for _ in range(R)]
    if solve():
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')