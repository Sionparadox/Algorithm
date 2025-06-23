import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
stack = []
answer = [0]*N
for i in range(N):
    h = towers[i]
    while stack and stack[-1][0] <= h:
        stack.pop()
    
    if stack:
        answer[i] = stack[-1][1]
    stack.append((h, i+1))

print(' '.join(map(str, answer)))

'''
monotonic stack
h이하는 다 pop
'''
