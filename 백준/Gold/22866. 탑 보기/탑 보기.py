import sys
input = sys.stdin.readline

N = int(input())
height = list(map(int, input().split()))

result= [[0, 0] for _ in range(N)]
stack = []
for i in range(N):
    h = height[i]
    while stack and height[stack[-1]] <= h:
        stack.pop()
    
    if stack:
        result[i][0] += len(stack)
        result[i][1] = stack[-1] + 1
    stack.append(i)

stack = []
for i in range(N-1, -1, -1):
    h = height[i]
    while stack and height[stack[-1]] <= h:
        stack.pop()
    
    if stack:
        if result[i][0] == 0 or abs(stack[-1] - i) < abs(result[i][1]-i-1):
            result[i][1] = stack[-1] + 1
        result[i][0] += len(stack)
    stack.append(i)

for cnt, num in result:
    if cnt == 0:
        print(0)
    else:
        print(cnt, num)

'''
높이를 왼쪽 -> 오른쪽으로 돌며 스택에 쌓고
스택에 나보다 낮은 높이를 pop
이후 스택이 남았다면 개수를 스택 길이만큼 증가, 해당 노드를 가까운 노드로 설정
위 과정을 오른쪽 -> 왼쪽으로 한번 더 함
'''