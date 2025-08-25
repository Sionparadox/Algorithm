import sys
input = sys.stdin.readline

_input = input().strip()
L = len(_input)

suffix = [_input[i:] for i in range(L)]
suffix.sort()

answer = 0
for i in range(L-1):
    a, b = suffix[i], suffix[i+1]
    k = 0
    limit = min(len(a), len(b))
    while k < limit and a[k] == b[k]:
        k += 1
    answer = max(answer, k)

print(answer)        