import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
rest = [0]+sorted(map(int, input().split()))+[L]

left = 1
right = L
answer = L

while left<=right:
    mid = (left+right)//2
    
    cnt = 0
    for i in range(N+1):
        d = rest[i+1]-rest[i]
        cnt += (d-1)//mid
    
    if cnt <= M:
        right = mid-1
        answer = mid
    else:
        left = mid+1

print(answer)
'''
최대 길이애 대해 이분탐색
'''