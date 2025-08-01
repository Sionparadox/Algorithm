import sys
input = sys.stdin.readline
MOD = 1_000_000

N = int(input())

def mat_mul(a, b):
    return [[(a[0][0]*b[0][0]+a[0][1]*b[1][0])%MOD, (a[0][0]*b[0][1]+a[0][1]*b[1][1])%MOD],
            [(a[1][0]*b[0][0]+a[1][1]*b[1][0])%MOD, (a[1][0]*b[0][1]+a[1][1]*b[1][1])%MOD]]

def mat_pow(matrix, n):
    res = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            res = mat_mul(res, matrix)
        matrix = mat_mul(matrix, matrix)
        n //=2
    return res


def fib(n):
    if n == 0:
        return 0
    mat = [[1,1],[1,0]]
    res = mat_pow(mat, n-1)
    return res[0][0]%MOD

print(fib(N))
