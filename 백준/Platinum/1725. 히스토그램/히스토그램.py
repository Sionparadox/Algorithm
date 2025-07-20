import sys
input = sys.stdin.readline

N = int(input())
height = [int(input()) for _ in range(N)]+[0]

stack = []
answer = 0
for i in range(N+1):
    h = height[i]
    left = i
    while stack and stack[-1][1] >= h :
        idx, hh = stack.pop()
        answer = max(answer, hh*(i - idx))
        left = idx
    
    stack.append((left, h))

print(answer)
        