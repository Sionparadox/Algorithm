import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(N)]

answer = 0
for r in range(N):
    if sum(board[r]) % 2 == 1:
        board[r] = [1-x for x in board[r]]
        answer += 1

board = list(map(list, zip(*board[::-1])))
tmp = 0
for c in range(M):
    if sum(board[c]) % 2 == 1:
        tmp += 1

answer += tmp
if tmp % 2 == 0:
    print(min(answer, M+N-answer))
else:
    print(-1)

'''
몇개의 행, 열을 건드려야 하는지 찾기
홀수인 행을 다 뒤집기 -> 열에 대해 적용 -> 열을 뒤집을 수가 짝수면 성공
But, 반대인 경우가 최적일 수 있음 M+N-ans

111
011
001

000
011
110

101
110
011
'''