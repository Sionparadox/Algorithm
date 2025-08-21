import sys
input = sys.stdin.readline
MAX = 2_147_483_647

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def get_cnt(k):
    res = 0
    for A, C, B in arr:
        if k >= A:
            res += (min(k, C) - A)//B + 1
    return res

l, r = 0, MAX+1
while l<r:
    mid = (l+r)//2
    if get_cnt(mid) % 2 == 1:
        r = mid
    else:
        l = mid+1

if l > MAX:
    print("NOTHING")
else:
    print(l, get_cnt(l)-get_cnt(l-1))

'''
이분탐색으로 k를 구함.
k이하의 수의 개수를 셈.
홀수면 답이 k이하 아니면 k초과
'''