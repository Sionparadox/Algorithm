import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))
    even = 0
    odd = 0
    for num in nums[1:]:
        if num % 2 == 0:
            even += num
        else :
            odd += num
    if even > odd:
        print('EVEN')
    elif even < odd:
        print('ODD')
    else:
        print("TIE")