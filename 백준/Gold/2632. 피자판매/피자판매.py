import sys
from collections import defaultdict
input = sys.stdin.readline

K = int(input())
N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(M)]

def count_piece(pizza):
    L = len(pizza)
    res = defaultdict(int)
    if sum(pizza)<=K:
        res[sum(pizza)] = 1
    
    prefix = [0]*(2*L+1)
    for i in range(2*L):
        prefix[i+1] = prefix[i] + pizza[i % L]
    
    for l in range(1, L):
        for i in range(L):
            size = prefix[i+l] - prefix[i]
            if size <= K:
                res[size] += 1
    return res

pieceA = count_piece(A)
pieceB = count_piece(B)
answer = pieceA[K] + pieceB[K]

for k, cnt in pieceA.items():
    if k == K:
        continue
    
    answer += cnt*pieceB[K-k]

print(answer)

'''
기존 조각 배열에 앞에서부터 N-2개를 덧붙여서 계산.
N이 최대 1000이기 때문에 메모리 문제 x
최대 1000^2번 탐색*2 + 200만번 탐색 = 400만번 연산 << 가능?
'''