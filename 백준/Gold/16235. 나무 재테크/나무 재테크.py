import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
food = [list(map(int, input().split())) for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]
farm = [[5]*N for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def simulate(n):
    waits = []
    left = n
    for r in range(N):
        for c in range(N):
            if trees[r][c]:
                queue = deque()
                dead = 0
                for _ in range(len(trees[r][c])):
                    age = trees[r][c].popleft()
                    if farm[r][c] >= age:
                        farm[r][c] -= age
                        age += 1
                        queue.append(age)
                        if age % 5 == 0:
                            for dr, dc in directions:
                                nr, nc = r+dr, c+dc
                                if 0<=nr<N and 0<=nc<N:
                                    waits.append((nr, nc))
                    else:
                        dead += age//2
                        left -= 1
                
                trees[r][c] = queue
                farm[r][c] += dead
            farm[r][c] += food[r][c] 
    for r, c in waits:
        trees[r][c].appendleft(1)
        left += 1
    return left
    
answer = M
for _ in range(K):
    answer = simulate(answer)

print(answer)
