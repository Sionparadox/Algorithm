TC = int(input())
for tc in range(1, TC+1):
    L = int(input())
    S = input()
    
    SA = list(range(L))
    rank = [ord(ch) for ch in S]
    
    k = 1
    while k < L:
        SA.sort(key = lambda x: (rank[x], rank[x+k] if x+k<L else -1))
        tmp = [0]*L
        tmp[SA[0]] = 0
        for i in range(1, L):
            prev, curr = SA[i-1], SA[i]
            pk = (rank[prev], rank[prev+k] if prev+k<L else -1)
            ck = (rank[curr], rank[curr+k] if curr+k<L else -1)
            tmp[curr] = tmp[prev] if pk == ck else tmp[prev] + 1
        
        rank = tmp
        if rank[SA[-1]] == L-1:
            break
        k *= 2
    
    rank = [0]*L
    for i in range(L):
        rank[SA[i]] = i
    
    answer = k = 0
    for i in range(L):
        if rank[i] == 0:
            k = 0
            continue
        
        j = SA[rank[i]-1]
        while i+k<L and j+k<L and S[i+k] == S[j+k]:
            k += 1
        answer = max(answer, k)
        if k>0:
            k -= 1

    print(f'#{tc} {answer}')