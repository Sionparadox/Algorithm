import sys
input = sys.stdin.readline
MOD = 1000

N, B = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]


def multiply(X, Y):
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] = (res[i][j] + X[i][k]*Y[k][j])%MOD
    return res


def solve(matrix, power):
    if power == 1:
        return [[x % MOD for x in row] for row in matrix]
        
    half = solve(matrix, power//2)
    res = multiply(half, half)
    if power % 2 == 1:
        res = multiply(res, matrix)
    return res

answer = solve(matrix, B)
print('\n'.join([' '.join(map(str, line)) for line in answer]))