import sys
input = sys.stdin.readline

L, R = input().split()
answer = 0
if len(L) == len(R):
    for i in range(len(L)):
        if L[i] != R[i]:
            break
        if L[i] == '8':
            answer += 1

print(answer)    