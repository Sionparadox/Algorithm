import sys
from collections import Counter
input = sys.stdin.readline

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
time = 0

def transpose(arr):
    return list(map(list, zip(*arr)))

def solve(arr):
    R = len(arr)
    C = len(arr[0])
    if R<C:
        arr = transpose(arr)
    
    maxLen = 0
    res = []
    for row in arr:
        temp = []
        counter = Counter(row)
        for k,v in counter.items():
            if k == 0: continue
            temp.append((k, v))
        temp.sort(key=lambda x:(x[1], x[0]))
        sorted_arr = [x for pair in temp for x in pair][:100]
        res.append(sorted_arr)
        maxLen = max(maxLen, len(sorted_arr))
    
    for row in res:
        while len(row)<maxLen:
            row.append(0)
    
    if R<C:
        res = transpose(res)
    
    return res

while time<=100:
    if r<=len(arr) and c<=len(arr[0]) and arr[r-1][c-1] == k:
        break
    time += 1
    arr = solve(arr)
    
    
print(time if time<=100 else -1)
