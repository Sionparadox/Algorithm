def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    while len(people) > answer:
        if(people[-1] <= limit-people[answer]):
            people.pop()
        answer += 1
    return answer