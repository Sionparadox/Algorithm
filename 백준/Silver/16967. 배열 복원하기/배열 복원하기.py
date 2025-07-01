import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H+X)]
answer = [[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i<X or j<Y:
            answer[i][j] = arr[i][j]
        else:
            answer[i][j] = arr[i][j] - answer[i-X][j-Y]

print('\n'.join(' '.join(map(str, row)) for row in answer))
            