import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
minNum = min(min(row) for row in board)
maxNum = max(max(row) for row in board)


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def BFS(low, high):
    visited = [[False]*N for _ in range(N)]
    queue = deque([(0, 0)])
    visited[0][0] = True
    while queue:
        r, c = queue.popleft()
        if r == N-1 and c == N-1:
            return True
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if visited[nr][nc]:
                continue
            if low<=board[nr][nc]<=high:
                visited[nr][nc] = True
                queue.append((nr, nc))

    return False

def check(k):
    for i in range(minNum, maxNum-k+1):
        j = i+k
        if not (i<=board[0][0]<=j and i<=board[N-1][N-1]<=j):
            continue
        if BFS(i, i+k):
            return True
    return False

s = 0
e = maxNum-minNum
while s<e:
    mid = (s+e)//2
    if check(mid):
        e = mid
    else:
        s = mid+1

print(s)

'''
이분탐색으로 차이를 탐색하며 BFS로 가능한지 검사
'''