import sys
input = sys.stdin.readline

MOD = 900528

letters = input().rstrip()
target = input().rstrip()
L = len(letters)
T = len(target)
answer = 0
for i in range(T):
    idx = T-i-1
    n = letters.find(target[idx])+1
    tmp = (n * pow(L, i, MOD)) % MOD
    answer = (answer + tmp) % MOD

print(answer)

'''
문자열 길이 진법으로 생각.
L진법이지만 계산시에는
1~L을 사용(각 문자의 인덱스+1)
'''