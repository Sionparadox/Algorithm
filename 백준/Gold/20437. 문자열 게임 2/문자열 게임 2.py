import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    W = input().strip()
    K = int(input())
    pos = defaultdict(list)
    L = len(W)
    for i in range(L):
        pos[W[i]].append(i)
    minLen = L
    maxLen = 0
    for v in pos.values():
        V = len(v)
        if V < K:
            continue
        for i in range(V-K+1):
            minLen = min(minLen, v[i+K-1]-v[i]+1)
            maxLen = max(maxLen, v[i+K-1]-v[i]+1)
    if maxLen == 0:
        print(-1)
    else:
        print(minLen, maxLen)
