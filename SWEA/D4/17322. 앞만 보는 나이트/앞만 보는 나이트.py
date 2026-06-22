MOD = 1_000_000_007
MAX = 666666
factorial = [1]*(MAX+1)
for i in range(2, MAX+1):
    factorial[i] = (factorial[i-1]*i)%MOD

TC = int(input())
for tc in range(1, TC+1):
    X, Y = map(int, input().split())
    diff = abs(X-Y)
    k = min(X, Y)-diff
    if k<0 or k % 3 != 0:
        answer = 0
    else:
        m = (min(X, Y)-diff)//3
        n = m+diff
        inverse = pow((factorial[m]*factorial[n]) % MOD, MOD-2, MOD)
        answer = factorial[m+n]*inverse % MOD
    print(f'#{tc} {answer}')