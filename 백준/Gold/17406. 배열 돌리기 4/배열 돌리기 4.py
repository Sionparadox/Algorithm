import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmd = [tuple(map(int, input().split())) for _ in range(K)]

def rotate(r, c, depth, ar):
    r, c = r-1, c-1
    arr = [row[:] for row in ar]
    for d in range(1, depth+1):
        top, bottom = r-d, r+d
        left, right = c-d, c+d
        prev = arr[top][left]
        for col in range(left+1, right+1):
            arr[top][col], prev = prev, arr[top][col]
        for row in range(top+1, bottom+1):
            arr[row][right], prev = prev, arr[row][right]
        for col in range(right-1, left-1, -1):
            arr[bottom][col], prev = prev, arr[bottom][col]
        for row in range(bottom-1, top-1, -1):
            arr[row][left], prev = prev, arr[row][left]
    return arr

def DFS(arr, visit):
    global answer
    if len(visit) == K:
        answer = min(answer, min(sum(row) for row in arr))
        return
    
    copied = [row[:] for row in arr]
    for i in range(K):
        if str(i) in visit:
            continue
        r, c, depth = cmd[i]
        DFS(rotate(r, c, depth, copied), visit+str(i))
    
answer = float('inf')   
DFS(board, '')
print(answer)