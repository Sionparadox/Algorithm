import sys
input = sys.stdin.readline

N = int(input())

factor = 0
for i in range(2, int(N**0.5)+1):
    if N%i == 0:
        factor = N//i
        break


if factor == 0:
    print(N-1)
else:
    print(N-factor)

'''
가장 큰 약수(본인 제외)
루트 N까지만 탐색
루트N보다 큰 소수라면 N-1이 답
'''