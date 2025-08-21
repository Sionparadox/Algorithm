import sys
input = sys.stdin.readline

M, N = map(int, input().split())
universe = [list(map(int, input().split())) for _ in range(M)]
ordered = []

for i in range(M):
    arr = sorted(universe[i])
    temp = []
    for j in universe[i]:
        temp.append(arr.index(j)+1)
    universe[i] = temp

answer = 0
for i in range(M-1):
    for j in range(i+1, M):
        if universe[i] == universe[j]:
            answer += 1

print(answer)