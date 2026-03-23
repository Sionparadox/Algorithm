import sys
input = sys.stdin.readline

N = int(input())
a, b, c = map(int, input().split())
lu = a-b-c
ru = a+b+c
ld = a+b-c
rd = a-b+c

flag = (a+b+c) % 2
for _ in range(N-1):
    a, b, c = map(int, input().split())
    if (a+b+c) % 2 != flag:
        print("NO")
        exit(0)
    lu = max(lu, a-b-c)
    ru = min(ru, a+b+c)
    ld = max(ld, a+b-c)
    rd = min(rd, a-b+c)
    
    if lu>rd or ld>ru:
        print("NO")
        exit(0)

x = (lu+ld)//2
y = (ld-lu)//2
print(x, y)


'''
a, b, c인 개구리가 갈 수 있는 위치의 범위
c가 짝수일 때 현재 위치에서 c이하의 짝수거리인 위치 전부 가능
c가 홀수일 때 현재 위치에서 c이하의 홀수거리인 위치 전부 가능
-> a+b+c % 2가 전부 같아야함.
각각 개구리가 갈 수 있는 범위는 기울어진 정사각형(마름모) 형태
공통범위는 모든 마름모가 겹치는 부분.
한 개구리에 대해 x,y가 개구리 범위 안에 있으려면
|x-a| + |y-b| <= c

2, 3, 4
좌측 상 : (-2,3) ~ (2,7)
우측 상 : (6,3) ~ (2,7)
좌측 하 : (-2,3) ~ (2,-1)
우측 하 : (6,3) ~ (2,-1)

2, 3, 5:
좌측 상 : (-3,3) ~ (2,8)   x-y = a-b-c
우측 상 : (7,3) ~ (2,8)    x+y = a+b+c
좌측 하 : (-3,3) ~ (2,-2)  x+y = a+b-c
우측 하 : (7,3) ~ (2,-2)   x-y = a-b+c

a+b-c <= x+y <= a+b+c  (ld~ru)
a-b-c <= x-y <= a-b+c  (lu~rd)
좌상, 좌하를 연립한 값이 정답
'''