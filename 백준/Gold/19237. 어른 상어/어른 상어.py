import sys
from collections import deque
input = sys.stdin.readline

directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
N, M, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sharks = [[(-1, -1), -1] for  _ in range(M+1)]

smells = deque()
temp = []
for r in range(N):
    for c in range(N):
        if board[r][c] != 0:
            n = board[r][c]
            board[r][c] = n*k
            sharks[n][0] = (r, c)
            temp.append((r, c))
smells.append(temp)

see = list(map(int, input().split()))
for i in range(1, M+1):
    sharks[i][1] = see[i-1]

dir_info = [[] for _ in range(M+1)]
for i in range(1, M+1):
    dir_info[i] = [None]+[list(map(int, input().split())) for _ in range(4)]

def next_pos(num):
    (r, c), d = sharks[num]
    for dir in dir_info[num][d]:
        dr, dc = directions[dir]
        nr, nc = r+dr, c+dc
        if 0<=nr<N and 0<=nc<N and board[nr][nc] == 0:
            return (nr, nc, dir)
    
    for dir in dir_info[num][d]:
        dr, dc = directions[dir]
        nr, nc = r+dr, c+dc
        if 0<=nr<N and 0<=nc<N and (num-1)*k < board[nr][nc] <= num*k:
            return (nr, nc, dir)

queue = deque()
for i in range(1, M+1):
    queue.append(i)

time = 0
dead = set()
while queue and time < 1000:
    left = M - len(dead)
    if left == 1:
        break
    time += 1
    for _ in range(left):
        num = queue.popleft()
        nr, nc, nd = next_pos(num)
        sharks[num] = [(nr, nc), nd]
    
    temp = []
    for num in range(1, M+1):
        if num in dead:
            continue
        
        (r, c), _ = sharks[num]
        if board[r][c] == 0:
            board[r][c] = num*k
        elif board[r][c] > (num-1)*k:
            board[r][c] -= 1
        else:
            dead.add(num)
            continue
        temp.append((r, c))
        queue.append(num)
    smells.append(temp)

    if time>=k:
        pos = smells.popleft()
        for r, c in pos:
            if board[r][c] % k == 0:
                board[r][c] = 0
            else:
                board[r][c] += 1
    
print(time if M-len(dead) == 1 else -1)        
