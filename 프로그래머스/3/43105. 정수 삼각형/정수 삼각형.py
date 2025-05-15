def solution(triangle):
    for d in range(len(triangle)-2,-1,-1):
        for i in range(d+1):
            triangle[d][i] += max(triangle[d+1][i], triangle[d+1][i+1])
    return triangle[0][0]