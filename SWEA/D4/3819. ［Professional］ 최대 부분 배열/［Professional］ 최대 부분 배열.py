TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    max_value = 0
    answer = -float('inf')
    for n in arr:
        max_value = max(n, n+max_value)
        answer = max(answer, max_value)
    print(f'#{tc} {answer}')