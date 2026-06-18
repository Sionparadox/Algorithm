def check(k):
    w, h = 0, k
    for word in words:
        L = len(word)*k
        nw, nh = w+L, h+k
        if w != 0:
            nw += k
        if nw <= W:
            w = nw
        elif nh <= H and L <= W:
            h = nh
            w = L
        else:
            return False
    return True

TC = int(input())
for tc in range(1, TC+1):
    H, W, N = map(int, input().split())
    words = input().split()
    l, r = 0, min(H, W)
    answer = 0
    while l <= r:
        mid = (l+r)//2
        if check(mid):
            answer = mid
            l = mid+1
        else:
            r = mid-1
    print(f'#{tc} {answer}')