TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    x = N*(N+1)//2
    z = x*2
    y = z-N
    print(f'#{tc} {x} {y} {z}')