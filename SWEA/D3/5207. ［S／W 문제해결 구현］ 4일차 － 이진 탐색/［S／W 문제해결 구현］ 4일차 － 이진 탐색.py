def bisect(n):
    l, r = 0, N-1

    dir = 0
    while l <= r:
        mid = (l+r)//2
        if A[mid] == n:
            return True
        elif A[mid] < n:
            if dir == 1:
                return False
            dir = 1
            l = mid+1
        else:
            if dir == -1:
                return False
            dir = -1
            r = mid-1
    return False
    
            
TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    answer = 0
    for n in B:
        if bisect(n):
            answer += 1
    
    print(f'#{tc} {answer}')