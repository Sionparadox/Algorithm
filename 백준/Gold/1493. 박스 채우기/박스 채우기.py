import sys
input = sys.stdin.readline

L, W, H = map(int, input().split())
n = int(input())
cubes = {}
for _ in range(n):
    s, k = map(int, input().split())
    cubes[s] = k

answer = 0
filledArea = 0
for i in range(20, -1, -1):
    length = (1 << i)
    volume = length**3
    maxCnt = (L//length) * (W//length) * (H//length) - filledArea//volume
    if maxCnt <= 0:
        continue
    canUse = min(maxCnt, cubes.get(i, 0))
    answer += canUse
    filledArea += canUse * volume

if filledArea == L*W*H:
    print(answer)
else :
    print(-1)

'''
분할정복 << 시간초과
그리디로 해결해야할듯 -> 큰 큐브부터 채워나가기.
사용할 수 있는 큐브 개수를 계산
-> 전체 영역에서 넣을 수 있는 최대 큐브 수에서 이미 채워진 영역에 들어가는 큐브 수를 뺀 값.

'''
    