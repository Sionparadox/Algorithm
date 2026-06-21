MOD = 1234567891
MAX = 1_000_000
TC = int(input())
factorial = [1]*(MAX+1)
for i in range(2, MAX+1):
    factorial[i] = (factorial[i-1]*i)%MOD

for tc in range(1, TC+1):
    N, R = map(int, input().split())
    answer = factorial[N]
    
    tmp = (factorial[R]*factorial[N-R])%MOD
    tmp = pow(tmp, MOD-2, MOD)
    answer = (answer*tmp)%MOD
    print(f'#{tc} {answer}')
