import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split()))[1:] for _ in range(N)]
arr = arr+arr
now = [-1]*(M+1)

def binary_matching(node):
    for work in arr[node]:
        if visited[work]: continue
        visited[work] = True
        if now[work] == -1 or binary_matching(now[work]):
            now[work] = node
            return True
    
    return False

answer = 0
for i in range(2*N):
    visited = [False]*(M+1)
    if binary_matching(i):
        answer += 1
    if answer == M:
        break

print(answer)
