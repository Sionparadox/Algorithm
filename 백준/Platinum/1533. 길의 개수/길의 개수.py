import sys
input = sys.stdin.readline
MOD = 1_000_003

N, S, E, T = map(int, input().split())
matrix = [list(map(int, list(input().strip()))) for _ in range(N)]
S, E = S-1, E-1
M = 5

SIZE = N*M
mat = [[0]*SIZE for _ in range(SIZE)]
for r in range(N):
    for c in range(N):
        if matrix[r][c] == 0:
            continue
        mat[r][c+N*(matrix[r][c]-1)] = 1

for i in range(N):
    for j in range(1, M):
        mat[i+j*N][i+(j-1)*N] = 1

def mat_mul(A, B):
    res =[[0]*SIZE for _ in range(SIZE)]
    for r in range(SIZE):
        for c in range(SIZE):
            for k in range(SIZE):
                res[r][c] = (res[r][c] + A[r][k]*B[k][c]) % MOD
    return res

def mat_pow(A, k):
    if k == 1:
        return A
    
    half = mat_pow(A, k//2)
    res = mat_mul(half, half)
    if k % 2 == 1:
        res = mat_mul(res, A)
    
    return res

R = mat_pow(mat, T)
print(R[S][E])



'''
확장 행렬?
-> 가중치가 다른 행렬에 대해 가중치를 같게 만들어서 
거듭제곱시 각 항에 가해지는 가중치를 동일하게 하여
경우의 수를 계산할 수 있도록 함
:기본적으로 행렬의 거듭제곱은 1단계씩 동일하게 계산됨
이때 1이 아닌 값으로 시작하면 각각 항에 대해 다른 가중치로 계산됨.
이를 방지하기 위해 만듦
012
201
120
->
010001
001100
100010
100000
010000
001000
'''
