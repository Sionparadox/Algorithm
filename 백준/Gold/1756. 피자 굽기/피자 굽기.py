import sys
input = sys.stdin.readline

D, N = map(int, input().split())
width = list(map(int, input().split()))
pizzas = list(map(int, input().split()))

for i in range(1, D):
    width[i] = min(width[i], width[i-1])

p = 0
for i in range(D-1, -1, -1):
    if width[i] >= pizzas[p]:
        p += 1
    if p == N:
        print(i+1)
        exit(0)
print(0)
