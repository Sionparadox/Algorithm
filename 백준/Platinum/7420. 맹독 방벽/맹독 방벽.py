import sys
import math
input = sys.stdin.readline

N, L = map(int, input().split())
buildings = [tuple(map(int, input().split())) for _ in range(N)]
buildings.sort()

def CCW(i, j, k):
    x1, y1 = buildings[i]
    x2, y2 = buildings[j]
    x3, y3 = buildings[k]
    return (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)

def convex_hull():
    lower = []
    for i in range(N):
        while len(lower)>=2:
            if CCW(lower[-2], lower[-1], i) <= 0:
                lower.pop()
            else: break
        lower.append(i)
    
    upper = []
    for i in range(N-1, -1, -1):
        while len(upper)>=2:
            if CCW(upper[-2], upper[-1], i)<=0:
                upper.pop()
            else: break
        upper.append(i)
    
    return lower[:-1] + upper[:-1]

def distance(i, j):
    x1, y1 = buildings[i]
    x2, y2 = buildings[j]
    return ((x1-x2)**2 + (y1-y2)**2)**(0.5)

hull = convex_hull()
H = len(hull)

answer = 0

for i in range(H):
    answer += distance(hull[i], hull[(i+1)%H])

answer += 2*L*math.pi
print(round(answer))

'''
Convex Hull로 외곽을 이루는 점을 구함.
N각형일 경우 원형으로 이루어진 부분: 2pi
즉 문제의 요구사항 = 볼록껍질의 둘레 + 2pi
'''