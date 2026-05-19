T = int(input())
def dfs(curr, cnt, cost):
    global answer
    if cost >= answer:
        return
    if cnt == N:
        answer = min(answer, cost)
    
    for nxt in range(N):
        if visited[nxt]:
            continue
        visited[nxt] = True
        dfs(curr+1, cnt+1, cost+costs[curr][nxt])
        visited[nxt] = False
    

for t in range(1, T+1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    answer = float('inf')
    visited = [False]*N
    dfs(0, 0, 0)
    print(f'#{t} {answer}')