import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))
stack = []
answer = 0
for i in range(W):
    h = blocks[i]
    while stack and stack[-1][0] < h:
        height, idx = stack.pop()
        if not stack:
            break
        
        length = i-stack[-1][1]-1
        answer += (min(h, stack[-1][0]) - height) * length
        
    stack.append((h, i))
print(answer)

'''
monotonic stack
idx,h를 저장, pop할 때 스택 끝부분과 비교해서 높이, 너비 계산
'''