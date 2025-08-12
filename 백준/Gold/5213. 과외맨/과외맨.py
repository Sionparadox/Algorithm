import sys
import heapq
input = sys.stdin.readline

N = int(input())
board = []

for r in range(N):
    temp = []
    C = N
    if r % 2 == 1:
        C -= 1
    for c in range(C):
        a, b = map(int, input().split())
        temp.append(a)
        temp.append(b)
    if r % 2 == 1:
        temp = [0]+temp+[0]
    board.append(temp)

def number(r, c):
    res = r*N-(r//2)
    if r % 2 == 0:
        res += c//2    
    else:
        res += (c-1)//2
    return res + 1

even_directions = [(0, -2), (0, 2), (1, 0), (-1, 0), (1, 2), (-1, 2)] #짝수 행
odd_directions = [(0, -2), (0, 2), (1, 0), (-1, 0), (1, -2), (-1, -2)] #홀수 행

def check(r, c, nr, nc, d):
    if nr < 0 or nr >= N or nc < 0 or nc >= 2*N: return False
    if nr % 2 == 1 and (nc == 0 or nc == 2*N-1): return False
    
    if d in (2,3):
        if board[r][c] == board[nr][nc]: return True
        return False
    if r % 2 == 0:
        if d == 0:
            if board[r][c] == board[nr][nc+1]: return True
            return False
        if d == 1:
            if board[r][c+1] == board[nr][nc]: return True
            return False
        if board[r][c+1] == board[nr][nc-1]: return True
    if r % 2 == 1:
        if d == 0:
            if board[r][c-1] == board[nr][nc]: return True
            return False
        if d == 1:
            if board[r][c] == board[nr][nc-1]: return True
            return False
        if board[r][c-1] == board[nr][nc+1] : return True
    return False

def find_path():
    tot = N*N - N//2
    prev = [-1] * (tot + 1)
    prev[1] = 0
    pq = [(1, 0, 0)]
    max_num = 1
    
    while pq:
        dist, r, c = heapq.heappop(pq)
        k = number(r, c)
        if k > max_num:
            max_num = k   
        if k == tot:
            break
        
        directions = even_directions if r%2==0 else odd_directions
        for d in range(6):
            nr, nc = r+directions[d][0], c+directions[d][1]
            if check(r, c, nr, nc, d):
                nk = number(nr, nc)
                if prev[nk] != -1:
                    continue
                if k == nk:
                    continue
                prev[nk] = k
                heapq.heappush(pq, (dist + 1, nr, nc))
    
    path = []
    curr = max_num
    while curr != 0:
        path.append(curr)
        if curr == 1:
            break
        curr = prev[curr]
    
    path.reverse()
    return path

path = find_path()
print(len(path))
print(*path) 