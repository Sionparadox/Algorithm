from collections import Counter
def solution(participant, completion):
    d = Counter(participant) - Counter(completion)
    answer = list(d.keys())[0]
    return answer