import sys
input = sys.stdin.readline

def findPiece():
    l, r = 0, n-1
    while l<r:
        s = nums[l]+nums[r]
        if s == x:
            print(f'yes {nums[l]} {nums[r]}')
            return
        if s < x :
            l += 1
        else :
            r -= 1
    print('danger')
    return 

while True:
    try:
        x = int(input())
    except:
        break
    n = int(input())
    x *= 10000000
    nums = [int(input()) for _ in range(n)]
    nums.sort()
    findPiece()

'''
투포인터?
'''