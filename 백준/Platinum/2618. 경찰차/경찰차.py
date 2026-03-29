import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')

N = int(input())
W = int(input())
dp = [[-1]*(W+2) for _ in range(W+2)]

pos = [(1, 1), (N, N)] + [tuple(map(int, input().split())) for _ in range(W)]

def solve(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    nxt = max(x, y) + 1
    if nxt == W+2:
        return 0
    
    d1 = solve(nxt, y) + abs(pos[nxt][0] - pos[x][0]) + abs(pos[nxt][1] - pos[x][1])
    d2 = solve(x, nxt) + abs(pos[nxt][0] - pos[y][0]) + abs(pos[nxt][1] - pos[y][1])
    
    dp[x][y] = min(d1, d2)
    return dp[x][y]

def backTrack(x,y):
    nxt = max(x, y) + 1
    if nxt == W+2:
        return 0
    
    d1 = solve(nxt, y) + abs(pos[nxt][0] - pos[x][0]) + abs(pos[nxt][1] - pos[x][1])
    d2 = solve(x, nxt) + abs(pos[nxt][0] - pos[y][0]) + abs(pos[nxt][1] - pos[y][1])
    
    if dp[x][y] == d1:
        print(1)
        backTrack(nxt, y)
    else:
        print(2)
        backTrack(x, nxt)
    


print(solve(0, 1))
backTrack(0, 1)

'''
dp[i][j] : 경찰차가 각각 i,j번째 사건에 있을 때 최소거리
dp[0][1] : 시작
'''

