import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrixA = []
matrixB = []
for _ in range(N):
    _input = list(map(int ,list(input().rstrip())))
    matrixA.append(_input)

for _ in range(N):
    _input = list(map(int ,list(input().rstrip())))
    matrixB.append(_input)

def flip(r, c):
    for nr in range(r, r+3):
        for nc in range(c, c+3):
            matrixA[nr][nc] = 1-matrixA[nr][nc]

answer = 0
for r in range(N-2):
    for c in range(M-2):
        if matrixA[r][c] != matrixB[r][c]:
            flip(r, c)
            answer += 1

for r in range(N):
    for c in range(M):
        if matrixA[r][c] != matrixB[r][c]:
            answer = -1
            break
    if answer == -1:
        break

print(answer)