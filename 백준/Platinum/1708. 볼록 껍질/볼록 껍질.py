import sys

#양수일 때만 True(반시계)
def CCW(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) > (b[1]-a[1])*(c[0]-a[0])

N = int(input())
dots = [tuple(map(int, input().split())) for _ in range(N)]
dots.sort()

lower = []
for dot in dots:
    while len(lower)>=2 and not CCW(lower[-2], lower[-1], dot):
        lower.pop()
    lower.append(dot)

upper = []
for dot in dots[::-1]:
    while len(upper)>=2 and not CCW(upper[-2], upper[-1], dot):
        upper.pop()
    upper.append(dot)

print(len(lower) + len(upper) - 2)

'''
모든 점을 x값 기준으로 정렬(같다면 y기준)
0번 점은 반드시 볼록 껍질에 포함됨.

CCW로 판별 : ca와 ab를 외적(ad-bc)
반시계만 채택
'''