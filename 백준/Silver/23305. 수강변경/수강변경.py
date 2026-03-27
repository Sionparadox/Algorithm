import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

counter = Counter(A)
answer = 0
for i in B:
    if i not in counter:
        answer += 1
        continue
    counter[i] -= 1
    if counter[i]<0:
        answer += 1
print(answer)