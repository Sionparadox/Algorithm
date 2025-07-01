import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

def backTrack(row, col):
    if col == C-1:
        return True
    
    for dr, dc in ((-1, 1), (0, 1), (1, 1)):
        nr, nc = row+dr, col+dc
        if nr<0 or nr >=R:
            continue
        if board[nr][nc] == '.':
            board[nr][nc] = 'x'
            if backTrack(nr, nc):
                return True
    return False

answer = 0
for r in range(R):
    if backTrack(r, 0):
        answer += 1
print(answer)

'''
모든 파이프가 최대한 상단에 붙어서 움직이도록 함.
우상단, 우측, 우하단 순서로 검사. 백트래킹으로 짜서 앞선 파이프가 안될때 다음으로 넘어갈 수 있도록 짬
'''