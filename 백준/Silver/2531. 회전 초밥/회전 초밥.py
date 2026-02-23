import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
selected = [0]*(d+1)

cnt = 0
for i in range(k):
    n = sushi[i]
    if selected[n] == 0:
        cnt += 1
    selected[n] += 1

answer = cnt
if selected[c] == 0:
    answer += 1

for i in range(N):
    prev = sushi[i]
    curr = sushi[(i+k)%N]
    selected[prev] -= 1
    if selected[prev] == 0:
        cnt -= 1
    if selected[curr] == 0:
        cnt += 1
    selected[curr] += 1
    
    coupon = 1 if selected[c] == 0 else 0
    answer = max(answer, cnt+coupon)

print(answer)
