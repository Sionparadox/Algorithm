import sys
input = sys.stdin.readline

def CCW(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)

def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    a = CCW(x1, y1, x2, y2, x3, y3)
    b = CCW(x1, y1, x2, y2, x4, y4)
    c = CCW(x3, y3, x4, y4, x1, y1)
    d = CCW(x3, y3, x4, y4, x2, y2)
    if a*b < 0 and c*d < 0:
        return True
    return False

x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

if is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    print(1)
else:
    print(0)
