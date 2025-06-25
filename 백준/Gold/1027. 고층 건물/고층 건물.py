import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

seen = [0]*N
for i in range(N-1):
    for j in range(i+1, N):
        diff = (arr[j]-arr[i])/(j-i)
        if all([arr[k] < arr[i]+diff*(k-i) for k in range(i+1, j)]):
            seen[i] += 1
            seen[j] += 1

print(max(seen))