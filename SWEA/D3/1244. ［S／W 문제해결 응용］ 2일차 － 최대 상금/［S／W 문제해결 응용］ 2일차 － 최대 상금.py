def dfs(idx, k):
    global answer
    if k>N:
        return
    if idx == L:
        if not dup and (N-k)%2 == 1:
            num[-1], num[-2] = num[-2], num[-1]
            answer = max(answer, int(''.join(map(str, num))))
            num[-1], num[-2] = num[-2], num[-1]
        else:
            answer = max(answer, int(''.join(map(str, num))))
        return
    
    mx = max(num[idx:])
    if k == N or num[idx] == mx:
        dfs(idx+1, k)
        return
    
    for i in range(idx+1, L):
        if num[i] == mx:
            num[idx], num[i] = num[i], num[idx]
            dfs(idx+1, k+1)
            num[idx], num[i] = num[i], num[idx]
        

TC = int(input())
for tc in range(1, TC+1):
    num, N = input().split()
    num = list(map(int, list(num)))
    N = int(N)
    L = len(num)
    answer = 0
    dup = L != len(set(num))
    
    dfs(0, 0)
    print(f'#{tc} {answer}')