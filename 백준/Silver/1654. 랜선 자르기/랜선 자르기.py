import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

left = 1
right = max(lines)
answer = 0

while left <= right:
    mid = (left+right)//2
    
    cnt = 0
    for line in lines:
        cnt += line//mid
    
    if cnt < N:
        right = mid-1
    else:
        left = mid + 1
        answer = mid

print(answer)