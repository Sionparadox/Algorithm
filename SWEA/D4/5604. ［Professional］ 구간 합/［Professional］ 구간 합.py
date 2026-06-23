def solve(n):
    if n < 0: return 0
    res = 0
    i = 1
    while n > 0:
        r = n % 10
        n = n // 10
        s = sum(int(x) for x in str(n))
        tmp = r*(r+1)//2 + s*(r+1) + 45*(n)
        res += tmp * i
        i *= 10
        n -= 1
    return res
        
TC = int(input())
for tc in range(1, TC+1):
    A, B = map(int, input().split())
    print(f'#{tc} {solve(B) - solve(A-1)}')