def backtrack(cnt, left, right):
    global answer
    if cnt == N:
        answer += 1
        return
    remains = total-left-right
    
    if left>=right+remains:
        answer += 2**(N-cnt) * factorial[N-cnt]
        return
    
    for nxt in range(N):
        if not used[nxt]:
            used[nxt] = True
            if right+weights[nxt] <= left:
                backtrack(cnt+1, left, right+weights[nxt])
            backtrack(cnt+1, left+weights[nxt], right)
            used[nxt] = False
    
factorial = [1]*10
for i in range(1, 10):
    factorial[i] = factorial[i-1]*i

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    weights = list(map(int, input().split()))
    total = sum(weights)
    used = [False]*N
    answer = 0
    backtrack(0, 0, 0)
    print(f'#{tc} {answer}')