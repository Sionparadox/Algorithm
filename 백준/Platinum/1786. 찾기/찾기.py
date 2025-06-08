import sys
input = sys.stdin.readline

T = input().rstrip('\n')
P = input().rstrip('\n')

n = len(T)
m = len(P)

pi = [0]*m
j = 0
for i in range(1, m):
    while j>0 and P[i] != P[j]:
        j = pi[j-1]
    
    if P[i] == P[j]:
        j += 1
        pi[i] = j

answer = []
k = 0
for i in range(n):
    while k>0 and T[i] != P[k]:
        k = pi[k-1]
    if T[i] == P[k]:
        if k == m-1:
            answer.append(i-m+2)
            k = pi[k]
        else :
            k += 1

print(len(answer))
print('\n'.join(map(str, answer)))