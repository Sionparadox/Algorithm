TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    week = list(map(int, input().split()))
    s = sum(week)
    q, r = divmod(N, s)
    if r == 0:
        q -= 1
        r = s
    
    answer = q*7
    k = 7
    
    for d in range(7):
        if not week[d]: continue
        t = 0
        for i in range(7):
            if week[(d+i)%7]:
                t += 1
            if t == r:
                k = min(k, i+1)
                break
        
    answer += k
    print(f'#{tc} {answer}')