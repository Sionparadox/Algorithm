import sys
input = sys.stdin.readline

N, M = map(int,input().split())
if M<N:
    print(0)
elif M == N:
    print(M)
else:
    print(N+1)