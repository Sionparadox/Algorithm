T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    d = [abs(arr[i]-arr[i-1]) for i in range(1, N)]
    dd = [abs(arr[i]-arr[i-2]) for i in range(2, N)]
    ds = [d[i]+d[i+1] for i in range(N-2)]
    answer = sum(d)
    max_diff = 0
    for i in range(N-2):
        if max_diff < ds[i]-dd[i]:
            max_diff = ds[i]-dd[i]
    
    answer -= max_diff
    print(answer)
    
    