import sys
input = sys.stdin.readline

N, M, L, K = map(int, input().split())
stars = [list(map(int, input().split())) for _ in range(K)]
star_x = set()
star_y = set()

for x, y in stars:
    star_x.add(x)
    star_y.add(y)
star_x = sorted(list(star_x))
star_y = sorted(list(star_y))

answer = 0
for x in star_x:
    for y in star_y:
        cnt = 0
        for sx, sy in stars:
            if x <= sx <= x+L and y <= sy <= y+L:
                cnt += 1
        answer = max(answer, cnt)

print(K - answer)

'''
별의 x,y를 각각 저장해서 정렬.
이 x,y를 트램펄린의 시작점으로 해서 답을 구하기
x사이클 1, y사이클 1, 별이 안에 있는지 검사 사이클 1
K^3 >> 최대 100만번 연산
'''