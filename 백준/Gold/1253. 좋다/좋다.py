import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0

for i in range(N):
    s = 0
    e = N-1
    while s < e:
        t = arr[s]+arr[e]
        if t == arr[i]:
            if s == i:
                s += 1
            elif e == i:
                e -= 1
            else:
                cnt += 1
                break
        elif t < arr[i]:
            s += 1
        else:
            e -= 1

print(cnt)    