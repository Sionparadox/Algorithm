TC = int(input())
for tc in range(1, TC+1):
    N = list(input())
    L = len(N)
    max_v = min_v = int(''.join(N))
    for i in range(L-1):
        for j in range(i+1, L):
            if i == 0 and N[j] == '0':
                continue
            N[i], N[j] = N[j], N[i]
            k = int(''.join(N))
            max_v = max(max_v, k)
            min_v = min(min_v, k)
            N[i], N[j] = N[j], N[i]
    
    print(f'#{tc} {min_v} {max_v}')