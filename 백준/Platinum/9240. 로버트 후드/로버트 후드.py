import sys
input = sys.stdin.readline

C = int(input())
arrows = [tuple(map(int, input().split())) for _ in range(C)]
arrows.sort()

def CCW(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)
    

def convex_hull():
    lower = []
    for i in range(C):
        while len(lower)>=2:        
            if CCW(arrows[lower[-2]], arrows[lower[-1]], arrows[i]) <= 0:
                lower.pop()
            else : break
        lower.append(i)
    
    upper = []
    for i in range(C-1, -1, -1):
        while len(upper)>=2:        
            if CCW(arrows[upper[-2]], arrows[upper[-1]], arrows[i]) <= 0:
                upper.pop()
            else : break
        upper.append(i)
    
    return lower[:-1] + upper[:-1]

def distance(i, j):
    x1, y1 = arrows[i]
    x2, y2 = arrows[j]
    return (x1-x2)**2+(y1-y2)**2

hull = convex_hull()
H = len(hull)

answer = 0
r = 1
for l in range(H):
    ls = arrows[hull[l]]
    le = arrows[hull[(l+1)%H]]
    while True:
        rs = arrows[hull[r%H]]
        re = arrows[hull[(r+1)%H]]
        re = (re[0]-rs[0]+ls[0], re[1]-rs[1]+ls[1])
        if CCW(ls, le, re) > 0:
            r += 1
        else: break
    answer = max(answer, distance(hull[l], hull[r%H]))
    l += 1
    
print(answer**(0.5))