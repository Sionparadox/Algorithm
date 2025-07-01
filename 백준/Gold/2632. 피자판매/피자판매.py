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
    
    arr = pizza+pizza[:-2]
    for l in range(1, L):
        for i in range(L):
            size = sum(arr[i:i+l])
            if size <= K:
                res[size] += 1

    return res

pieceA = count_piece(A)
pieceB = count_piece(B)
answer = pieceA[K] + pieceB[K]

for k in range(1, K):
    answer += pieceA[k]*pieceB[K-k]

print(answer)

'''
기존 조각 배열에 앞에서부터 N-2개를 덧붙여서 계산.
N이 최대 1000이기 때문에 메모리 문제 x
최대 1000^2번 탐색*2 + 200만번 탐색 = 400만번 연산 << 가능?
'''