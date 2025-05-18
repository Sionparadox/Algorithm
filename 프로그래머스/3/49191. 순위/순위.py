from functools import reduce
def solution(n, results):
    answer = 0
    graph = [[False]*n for _ in range(n)]
    
    for A, B in results:
        graph[A-1][B-1] = True
    for i in range(n):
        graph[i][i] = True
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True
    
    for i in range(n):
        for j in range(n):
            if not graph[i][j] and not graph[j][i]:
                break
            
            if j == n-1: answer += 1
            
    return answer

