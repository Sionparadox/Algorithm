def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for num in B:
        while A and A[-1] >= num:
            A.pop()
        if A and A[-1] < num:
            A.pop()
            answer += 1
        
    return answer