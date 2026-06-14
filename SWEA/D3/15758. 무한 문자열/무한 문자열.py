import math
TC = int(input())
for tc in range(1, TC+1):
    S, T = input().split()
    N, M = len(S), len(T)
    k = math.gcd(N, M)
    if S*(M//k) == T*(N//k):
        print(f'#{tc} yes')
    else:
        print(f'#{tc} no')