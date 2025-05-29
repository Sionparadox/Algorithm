import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = int(Y*100/X)
if Z>=99:
    print(-1)
    exit()
s = 0
e = 1000000000

while s<e:
    mid = int((s+e)/2)
    rate = int((Y+mid)*100 / (X+mid))
    if rate == Z:
        s = mid+1
    else :
        e = mid
        
print(s)