import sys
input = sys.stdin.readline

N = int(input())
A, B= map(int, input().split())
M = int(input())
arr = [int(input()) for _ in range(M)]

dp = [[[-1]*(N+1) for _ in range(N+1)] for _ in range(M+1)]

def solve(idx, a, b):
    if idx == M:
        return 0
    
    if dp[idx][a][b] != -1:
        return dp[idx][a][b]
    
    curr = arr[idx]
    
    left = abs(a-curr) + solve(idx+1, curr, b)
    right = abs(b-curr) + solve(idx+1, a, curr)
    
    dp[idx][a][b] = min(left, right)
    return dp[idx][a][b]

print(solve(0, A, B))


'''
백트래킹? : 2^20 -> 1,000,000
dp를 사용해서 early return

dp[i][j][k] : i번째 입력에 대해 j,k문이 열려있을 이동횟수의 최소값
'''