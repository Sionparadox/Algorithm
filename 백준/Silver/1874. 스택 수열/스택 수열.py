import sys
input = sys.stdin.readline

N = int(input())
stack = []

k = 1
answer = []
for _ in range(N):
    n = int(input())
    while k<=n:
        stack.append(k)
        answer.append('+')
        k += 1
    
    if stack[-1] == n:
        stack.pop()
        answer.append('-')

if stack:
    print('NO')
else:
    for c in answer:
        print(c)