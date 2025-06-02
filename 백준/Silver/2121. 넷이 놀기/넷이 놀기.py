import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())

pos = [tuple(map(int, input().split())) for _ in range(N)]

posSet = set(pos)
answer = 0
for p in pos:
    x, y = p
    if (x+A, y) in posSet and (x, y+B) in posSet and (x+A, y+B) in posSet:
        answer += 1
print(answer)