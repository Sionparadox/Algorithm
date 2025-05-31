import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

value = sum(visitors[:X])
maxVal = value
cnt = 1
for i in range(N-X):
    e = i+X
    value += visitors[e] - visitors[i]
    if maxVal == value:
        cnt += 1
    elif maxVal < value:
        maxVal = value
        cnt = 1

if maxVal == 0:
    print('SAD')
else:
    print(maxVal)
    print(cnt)