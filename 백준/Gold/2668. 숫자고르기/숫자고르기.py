import sys
input = sys.stdin.readline

N = int(input())
nums = [0]+[int(input()) for _ in range(N)]

res = set()
def DFS(start, now, path):
    if visited[now]:
        if start == now:
            res.update(path)
        return
    visited[now] = True
    path.append(now)
    DFS(start, nums[now], path)

for i in range(1, N+1):
    visited = [False]*(N+1)
    DFS(i, i, [])

print(len(res))
print('\n'.join(map(str, sorted(res))))