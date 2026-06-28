INF = float('inf')
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_value = 0
    answer = -INF
    for n in arr:
        max_value = max(n, max_value+n)
        answer = max(answer, max_value)
    
    print(f'#{tc} {answer}')