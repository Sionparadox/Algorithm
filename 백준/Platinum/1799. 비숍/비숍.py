import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

black = []
white = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            if (i+j) % 2 == 0:
                black.append((i,j))
            else :
                white.append((i, j))

diag1 = [False]*(2*N-1)
diag2 = [False]*(2*N-1)
def backTrack(idx, k, color):
    global answer
    if idx == len(color):
        return k
    
    res = 0
    r, c = color[idx]
    if not diag1[r+c] and not diag2[r-c+N-1]:
        diag1[r+c] = True
        diag2[r-c+N-1] = True
        res = max(res, backTrack(idx+1, k+1, color))
        diag1[r+c] = False
        diag2[r-c+N-1] = False
    
    res = max(res, backTrack(idx+1, k, color))
    return res
answer = 0
answer += backTrack(0, 0,black)
answer += backTrack(0, 0,white)
print(answer)

'''
대각선 체크 bishops에 대해 (r-r1), (c-c1) 비교 << 시간초과
대각선 배열 활용해서 개선
diag1[i] : '/' r+c값이 일정
diag2[i] : '\' r-c값이 일정 but 음수 일 수 있으므로 N-1을 더해줌
'''
    