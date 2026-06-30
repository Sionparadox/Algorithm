from bisect import bisect_left

def search(k):
    idx = bisect_left(horse, k)
    left = right = float('inf')
    if idx > 0:
        left = abs(horse[idx-1]-k)
    if idx < M:
        right = abs(horse[idx]-k)
    
    if left == right:
        return left, 2
    else:
        return min(left, right), 1
    
    
TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    c1, c2 = map(int, input().split())
    cow = list(map(int, input().split()))
    horse = sorted(map(int, input().split()))
    dist = abs(c1-c2)
    min_dist = float('inf')
    ans = 0
    for c in cow:
        d, cnt = search(c)
        if d == min_dist:
           ans += cnt
        elif d < min_dist:
            min_dist = d
            ans = cnt
        
    print(f'#{tc} {dist+min_dist} {ans}') 