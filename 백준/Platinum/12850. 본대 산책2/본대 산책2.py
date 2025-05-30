import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MOD = 1000000007
#정과, 미래, 전산, 신앙, 한경, 형남, 진리, 학생
road = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]

def multiply(A, B):
    L = len(A)
    res = [[0]*L for _ in range(L)]
    for r in range(L):
        for c in range(L):
            for k in range(L):
                res[r][c] += A[r][k]*B[k][c]
                res[r][c] %= MOD
    return res
                
                
def mat_pow(A, d):
    if d == 1:
        return A
    
    half = mat_pow(A, d//2)
    res = multiply(half, half)
    if d % 2 == 0:
        return res
    else :
        return multiply(res, A)

D = int(input())
answer = mat_pow(road, D)
print(answer[0][0])