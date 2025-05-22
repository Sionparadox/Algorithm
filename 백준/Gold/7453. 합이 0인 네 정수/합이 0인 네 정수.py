import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
A = []
B = []
C = []
D = []
for _ in range(N):
    a,b,c,d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = []
CD = []
for i in range(N):
    for j in range(N):
        AB.append(A[i]+B[j])
        CD.append(C[i]+D[j])

CD = Counter(CD)
answer = 0
for i in AB:
    answer += CD[i*(-1)]
print(answer)
