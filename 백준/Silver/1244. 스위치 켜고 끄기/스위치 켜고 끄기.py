import sys
input = sys.stdin.readline

N = int(input())
light = [-1]+list(map(int, input().split()))
M = int(input())

def mul(n):
    for i in range(n, N+1, n):
        light[i] = 1-light[i]
    
def interval(n):
    light[n] = 1-light[n]
    i = 1
    while i<n<=N-i:
        if light[n-i] != light[n+i]:
            break
        light[n-i] = 1-light[n-i]
        light[n+i] = 1-light[n+i]
        i += 1

for _ in range(M):
    gender, idx = map(int, input().split())
    if gender == 1:
        mul(idx)
    else:
        interval(idx)

for i in range(1, N+1):
    print(light[i], end=' ')
    if i%20 == 0:
        print()