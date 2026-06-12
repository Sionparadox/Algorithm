directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
def check():
    for r in range(N):
        for c in range(N):
            if board[r][c] == '.':
                continue
            for dr ,dc in directions:
                max_r, max_c = r+dr*4, c+dc*4
                if max_r<0 or max_r>=N or max_c<0 or max_c>=N:
                    continue
                flag = True
                for i in range(1,5):
                    nr, nc = r+dr*i, c+dc*i
                    if board[nr][nc] == '.':
                        flag = False
                        break
                if flag:
                    return True
    
    return False

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    board = [input() for _ in range(N)]
    print(f"#{tc} {'YES' if check() else 'NO'}")
                
                