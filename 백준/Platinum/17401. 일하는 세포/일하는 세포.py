import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MOD = 1_000_000_007


T, N, D = map(int ,input().split())
graph = [[[0]*N for _ in range(N)]for _ in range(T)]
for t in range(T):
    M = int(input())
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[t][a-1][b-1] = c

def mat_mul(A, B):
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] = (res[i][j] + A[i][k]*B[k][j])%MOD
    return res

def mat_pow(A, k):
    if k <= 1:
        return A
    
    half = mat_pow(A, k//2)
    res = mat_mul(half, half)
    if k % 2 == 1:
        res = mat_mul(res, A)
    return res

cycle = [[int(i == j) for j in range(N)] for i in range(N)]
if D >= T:
    for t in range(T):
        cycle = mat_mul(cycle, graph[t])

answer = mat_pow(cycle, D//T)
for t in range(D%T):
    answer = mat_mul(answer, graph[t])

for row in answer:
    print(*row)