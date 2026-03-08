import sys
input = sys.stdin.readline

M, N = map(int, input().split())

def sorted_planet(arr):
    sorted_arr = sorted(set(arr))
    indexes = {v:i for i, v in enumerate(sorted_arr)}
    return tuple(indexes[x] for x in arr)

planet_idx = [sorted_planet(list(map(int, input().split()))) for _ in range(M)]

counter = {}
for t in planet_idx:
    if t in counter:
        counter[t] += 1
    else:
        counter[t] = 1

answer = 0
for value in counter.values():
    answer += value*(value-1)//2

print(answer)