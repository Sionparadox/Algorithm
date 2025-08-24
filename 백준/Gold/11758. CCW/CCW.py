import sys
input = sys.stdin.readline

def CCW(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
answer = CCW(x1, y1, x2, y2, x3, y3)
if answer == 0:
    print(0)
elif answer > 0:
    print(1)
else:
    print(-1)