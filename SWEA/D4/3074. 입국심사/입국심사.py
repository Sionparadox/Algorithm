def check(k):
    cnt = 0
    for time in arr:
        cnt += k//time
    return cnt >= M

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    left, right = 1, M*max(arr)
    answer = 1
    while left <= right:
        mid = (left+right)//2
        if check(mid):
            answer = mid
            right = mid-1
        else:
            left = mid + 1

    print(f"#{tc} {answer}")