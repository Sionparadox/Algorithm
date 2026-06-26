TC = int(input())
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
for tc in range(1, TC+1):
    S = input()
    d = 0
    x, y = 0, 0
    answer = 0
    for _ in range(4):
        for ch in S:
            if ch == 'S':
                x, y = x+directions[d][0], y+directions[d][1]
                answer = max(answer, x*x + y*y)
            elif ch == 'L':
                d = (d+1)%4
            elif ch =='R':
                d = (d-1)%4
    
    if x != 0 or y != 0:
        answer = 'oo'
    print(f'#{tc} {answer}')