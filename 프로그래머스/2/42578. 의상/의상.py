from collections import Counter
def solution(clothes):
    answer = 1
    count = Counter(cloth[1] for cloth in clothes)
    for n in list(count.values()):
        answer *= n+1
    return answer-1