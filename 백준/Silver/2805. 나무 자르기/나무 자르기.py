import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
answer = 0

while left <= right:
    mid = (left+right)//2
    
    k = 0
    for tree in trees:
        if tree > mid:
            k += tree-mid
    
    if k>=M:
        answer = mid
        left = mid+1
    else:
        right = mid-1

print(answer)
        