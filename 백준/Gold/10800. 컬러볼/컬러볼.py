import sys
input = sys.stdin.readline

N = int(input())

balls = []
for i in range(N):
    color, size = map(int,input().split())
    balls.append((size, color, i))
balls.sort()

tot = 0
prefix = [0]*(N+1)
answer = [0]*N
left = 0
for i in range(N):
    size, color, idx = balls[i]
    
    while balls[left][0] < size:
        s, c, _ = balls[left]
        tot += s
        prefix[c] += s
        left += 1
    answer[idx] = tot - prefix[color]

print('\n'.join(map(str, answer)))