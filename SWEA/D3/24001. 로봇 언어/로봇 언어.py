TC = int(input())
for _ in range(TC):
    S = input()
    L = 0
    R = 0
    answer = 0
    for c in S:
        if c == 'L':
            L += 1
            R -= 1
        elif c == 'R':
            L -= 1
            R += 1
        else:
            L += 1
            R += 1
        answer = max(answer, L, R)
    
    print(answer)
    