TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    for n in arr:
        q, r = divmod(n, 10)
        answer += pow(q, r)
    print(f'#{tc} {answer}')