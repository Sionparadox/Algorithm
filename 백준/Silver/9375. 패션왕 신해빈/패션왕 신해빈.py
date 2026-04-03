import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    cloth = defaultdict(int)
    for _ in range(N):
        key = input().split()[1]
        cloth[key] += 1
    
    res = 1
    for v in cloth.values():
        res *= (v+1)
    print(res-1)