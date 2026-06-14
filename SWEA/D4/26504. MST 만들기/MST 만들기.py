TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    min_v = sum(arr[:N-1])

    max_v = 0
    idx = 0
    for i in range(N-1):
        idx += i
        max_v += arr[idx]

    print(min_v, max_v)