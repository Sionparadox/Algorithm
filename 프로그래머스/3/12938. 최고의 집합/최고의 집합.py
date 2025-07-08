def solution(n, s):
    if s < n:
        return [-1]
    answer = []
    for i in range(n, 0, -1):
        val = s//i
        answer.append(val)
        s -= val
    
    return answer
