import sys
input = sys.stdin.readline

N, K = map(int, input().split())
weight = list(map(int, input().split()))

answer = 0
visited = [False]*N
def backTrack(val, day):
    global answer
    if day == N:
        answer += 1
        return
    
    for i in range(N):
        if visited[i]:
            continue
        
        new_val = val+weight[i]-K
        if new_val >= 500:
            visited[i] = True
            backTrack(new_val, day+1)
            visited[i] = False

backTrack(500, 0)
print(answer)