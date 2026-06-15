MAX = 1_000_000_000

def check(diff):
    arr = nums[:]
    for i in range(1, N):
        arr[i] = min(arr[i], arr[i-1]+diff)
    for i in range(N-1, 0, -1):
        arr[i-1] = min(arr[i-1], arr[i]+diff)
    return sum(nums) - sum(arr)

TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    l, r = 0, MAX
    answer = 0
    while l<=r:
        mid = (l+r)//2
        cnt = check(mid)
        if cnt<=K:
            r = mid-1            
            answer = mid
        else:
            l = mid+1
    
    print(f'#{tc} {answer}')
