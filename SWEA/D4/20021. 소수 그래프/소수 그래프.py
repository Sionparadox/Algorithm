is_prime = [True]*1501
is_prime[0] = is_prime[1] = False
for i in range(2, int(1501**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, 1501, i):
            is_prime[j] = False

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    for i in range(N, N+N//2+1):
        if is_prime[i]:
            answer = i
            break
    
    diff = answer - N
    edges = []
    for i in range(1, N+1):
        edges.append((i, i%N+1))
    
    used = set()
    for _ in range(diff):
        for u in range(1, N + 1):
            if u in used:
                continue
            for v in range(u + 2, N + 1):
                if v in used:
                    continue
                if v == u + 1:
                    continue
                edges.append((u, v))
                used.add(u)
                used.add(v)
                break
            else:
                continue
            break
    
    print(answer)
    for u, v in edges:
        print(u, v)