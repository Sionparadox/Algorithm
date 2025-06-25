import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

s = 1
e = arr[-1] - arr[0]
answer = 0
while s <= e:
    mid = (s+e)//2
    
    cnt = 1
    prev = arr[0]
    for pos in arr:
        if pos-prev >= mid:
            cnt += 1
            prev = pos
    
    if cnt < C:
        e = mid-1
    else:
        answer = mid
        s = mid+1
print(answer)