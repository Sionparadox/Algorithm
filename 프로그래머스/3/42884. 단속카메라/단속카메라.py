def solution(routes):
    answer = 0
    pos = -30001
    routes.sort(key= lambda x: x[1])
    for start, end in routes:
        if pos < start:
            pos = end
            answer += 1
            
    return answer;