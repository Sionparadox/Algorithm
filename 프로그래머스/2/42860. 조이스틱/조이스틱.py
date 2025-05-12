def solution(name):
    answer = sum([min(ord(n) - 65, 91 - ord(n)) for n in name])
    N = len(name)
    move = N-1
    for i in range(N):
        next = i+1
        while(next<N and name[next] == 'A'):
            next += 1
        move = min(move, i + N-next + min(i, N-next))
    answer += move
    return answer

