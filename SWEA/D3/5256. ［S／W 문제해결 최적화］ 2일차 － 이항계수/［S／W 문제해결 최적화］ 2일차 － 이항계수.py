T = int(input())
for t in range(1, T+1):
    n, a, b = map(int, input().split())
    k = min(a, b)
    res = 1
    x = 1
    for i in range(k):
        res *= (n-i)
        x *= (i+1)
    print(f'#{t} {res//x}')