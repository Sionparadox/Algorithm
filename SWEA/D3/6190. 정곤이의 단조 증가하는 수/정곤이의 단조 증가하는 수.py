TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = -1
    for i in range(N-1):
        for j in range(i+1, N):
            k = arr[i]*arr[j]
            prev = 9
            while k > 0 and prev >= k%10:
                prev = k % 10
                k //= 10
            
            if k == 0 :
                answer = max(answer, arr[i]*arr[j])
    
    print(f'#{tc} {answer}')