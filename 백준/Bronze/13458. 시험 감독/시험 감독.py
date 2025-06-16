import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for n in A:
    n -= B
    answer += 1
    if n>0:
        n *= -1
        answer += (n//C)*-1
        
print(answer)
