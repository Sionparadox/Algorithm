import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [int(input()) for _ in range(N)]
dice = [int(input()) for _ in range(M)]

pos = 0
answer = M
for i in range(M):
    pos += dice[i]
    if pos >= N:
        answer = i+1
        break
    pos += board[pos]
    if pos >= N:
        answer = i+1
        break

print(answer)