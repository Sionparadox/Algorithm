import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
boxes = [tuple(map(int, input().split())) for _ in range(M)]
boxes.sort(key=lambda x:(x[1],x[0]))

truck = [C]*(N+1)
answer = 0
for s, e, size in boxes:
    load = min(size, min(truck[s:e]))
    for i in range(s,e):
        truck[i] -= load
    answer += load

print(answer)