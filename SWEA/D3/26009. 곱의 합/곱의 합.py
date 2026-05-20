MOD = 998244353
TC = int(input())
for _ in range(TC):
    a, b, c = map(int, input().split())
    res = (a*(a+1)//2 * b*(b+1)//2 * c*(c+1)//2 ) % MOD
    print(res)