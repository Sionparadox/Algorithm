TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    res = round(N**(1/3))
    if res**3 != N:
        res = -1
    print(f'#{tc} {res}')