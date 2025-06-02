import sys
input = sys.stdin.readline

N, K, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(K)]

s = 1
e = N
def fruit(box):
    res = 0
    for A, B, C in arr:
        end = min(box, B)
        if end >= A:
            res += (end-A)//C+1
    return res

while s <= e:
    mid = (s+e)//2
    cnt = fruit(mid)
    if cnt >= D:
        e = mid-1
    else :
        s = mid+1
print(s)

'''
상자의 번호를 이분탐색
'''
