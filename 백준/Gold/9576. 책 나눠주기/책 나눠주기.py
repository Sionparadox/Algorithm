import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    rng = [tuple(map(int, input().split())) for _ in range(M)]
    rng.sort(key=lambda x:x[1])
    
    visited = [False]*(N+1)
    answer = 0
    
    for left, right in rng:
        for i in range(left, right+1):
            if not visited[i]:
                visited[i] = True
                answer += 1
                break
    
    print(answer)