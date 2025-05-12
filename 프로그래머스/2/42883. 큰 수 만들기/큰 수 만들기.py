def solution(number, k):
    numStack = []
    cnt = 0
    for i in range(len(number)):
        while len(numStack) != 0 and numStack[-1] < number[i] and cnt<k:
            numStack.pop()
            cnt += 1
        numStack.append(number[i])
    while cnt<k:
        numStack.pop()
        cnt += 1
    answer = ''.join(numStack)
    return answer
