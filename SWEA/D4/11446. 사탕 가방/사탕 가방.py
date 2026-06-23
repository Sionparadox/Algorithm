def check(n):
    if n == 0:
        return True
    res = 0
    for candy in candies:
        res += candy//n
    return res >= M

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    candies = list(map(int, input().split()))
    left, right = 0, sum(candies)//M
    answer = 0
    while left <= right:
        mid = (left+right)//2
        if check(mid):
            left = mid+1
            answer = mid
        else:
            right = mid-1

    print(f'#{tc} {answer}')