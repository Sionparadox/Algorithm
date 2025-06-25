import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

s = 0
cnt = 0
saved = set()
for i in range(N):
    while arr[i] in saved:
        saved.remove(arr[s])
        s += 1
    saved.add(arr[i])
    cnt += i-s+1

print(cnt)