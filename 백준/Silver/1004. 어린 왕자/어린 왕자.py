import sys
input = sys.stdin.readline

def inner(x, y, cx, cy, r):
    return (x-cx)**2+ (y-cy)**2 < r**2

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    answer = 0
    for _ in range(N):
        cx, cy, r = map(int, input().split())
        answer += 1 if inner(x1,y1,cx,cy,r) != inner(x2,y2,cx,cy,r) else 0
    print(answer)