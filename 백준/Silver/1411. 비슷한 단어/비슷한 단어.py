import sys
from collections import Counter
input = sys.stdin.readline

alpha = 'abcdefghijklmnopqrstuvwxyz'
def translate(str):
    d = {}
    idx = 0
    res = ''
    for c in str:
        if c not in d:
            d[c] = alpha[idx]
            idx += 1
        res += d[c]
    return res


N = int(input())
words = [translate(input().strip()) for _ in range(N)]
counter = Counter(words)
answer = 0
for v in counter.values():
    answer += v*(v-1)//2
print(answer)