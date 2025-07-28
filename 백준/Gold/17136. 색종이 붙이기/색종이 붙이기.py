import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(10)]
visited = [[False]*10 for _ in range(10)]
papers = {1:5, 2:5, 3:5, 4:5, 5:5}

answer = float('inf')

def checkSize(r, c, size):
    if r+size>10 or c+size>10:
        return False
    
    for i in range(r, r+size):
        for j in range(c, c+size):
            if board[i][j] == 0 or visited[i][j]:
                return False
    return True
            
def backTrack(pos, k):
    global answer
    if pos >= 100:
        answer = min(answer, k)
        return
    
    if k >= answer: return
    
    r, c = divmod(pos, 10)
    if board[r][c] == 0 or visited[r][c]:
        backTrack(pos+1, k)
        return
    
    for size in range(5, 0, -1):
        if papers[size]>0 and checkSize(r, c, size):
            for i in range(r, r+size):
                for j in range(c, c+size):
                    visited[i][j] = True
            papers[size] -= 1
            backTrack(pos+size, k+1)
            papers[size] += 1
            for i in range(r, r+size):
                for j in range(c, c+size):
                    visited[i][j] = False

backTrack(0, 0)
print(answer if answer != float('inf') else -1)