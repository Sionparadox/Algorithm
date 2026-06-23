def init(L, C):
    res = [0] * N

    for l in [C, L - 1 - C]:
        k = (l + 1) // N
        r = (l + 1) % N

        for i in range(N):
            res[i] += k
        for i in range(r):
            res[i] += 1

    res[0] -= 1
    return res

TC = int(input())
for tc in range(1, TC+1):
    X, Y, Z, A, B, C, N = map(int, input().split())
    DX = init(X, A)
    DY = init(Y, B)
    DZ = init(Z, C)
    xy = [0]*N
    answer = [0]*N
    for i in range(N):
        for j in range(N):
            xy[(i+j)%N] += DX[i]*DY[j]
    
    for i in range(N):
        for j in range(N):
            answer[(i+j)%N] += xy[i]*DZ[j]

    print(f'#{tc}', *answer)