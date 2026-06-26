MOD = 1_000_000_007
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    arr.sort(key = lambda x:(1-x[0])/x[1])
    answer = 1
    for a, b in arr:
        answer = (answer*a+b) % MOD
    print(f'#{tc} {answer}')