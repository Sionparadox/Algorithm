import sys
input = sys.stdin.readline

N = int(input())

i = 2
cnt = 0
while i**2 <= N:
    while N%i == 0:
        cnt += 1
        N //= i
    i += 1

if N > 1:
    cnt += 1

print("cubelover" if cnt == 2 else "koosaga")

'''
N이 1이나 소수 : 구사과 승
N을 소인수 분해했을때 소수의 수가 2개 : 큐브러버 승
-> 3개 이상일 경우 : 구사과 승
'''