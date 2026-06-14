TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    answer = arr[-1]-arr[0]
    for i in range(K-1, N):
        answer = min(answer, arr[i]-arr[i-K+1])
    print(f'#{tc} {answer}')
