import sys
input = sys.stdin.readline

M = int(input())
nums = [x-1 for x in list(map(int, input().split()))]
Q = int(input())
queries = []
for _ in range(Q):
    n, x = map(int, input().split())
    queries.append((n, x-1))

arr = [[-1]*M for _ in range(21)]
arr[0] = nums
for i in range(1, 21):
    for j in range(M):
        arr[i][j] = arr[i-1][arr[i-1][j]]

for n, x in queries:
    for i in range(20, -1, -1):
        if n & (1<<i):
            x = arr[i][x]
    print(x+1)