def solution(numbers, target):
    answer = 0
    L = len(numbers)
    
    def dfs(n, k):
        nonlocal answer
        if k == L:
            if n == target:
                answer += 1
            return
        dfs(n+numbers[k], k+1)
        dfs(n-numbers[k], k+1)
        
    dfs(0, 0)
    
    return answer
