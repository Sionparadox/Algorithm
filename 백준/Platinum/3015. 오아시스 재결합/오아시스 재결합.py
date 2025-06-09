import sys
input = sys.stdin.readline

N = int(input())

stack = []
answer = 0
for _ in range(N):
    p = int(input())
    cnt = 1
    while stack and stack[-1][0] < p:
        answer += stack.pop()[1]
    
    if stack and stack[-1][0] == p:
        cnt = stack[-1][1]
        answer += cnt
        cnt += 1
        stack.pop()
    if stack:
        answer += 1
    stack.append((p, cnt))

print(answer)

'''
한명씩 입력받으며
본인보다 작은 값들 다 pop 하면서 연속으로 등장한 길이만큼 더해줌

또한 스택끝이 나와 같다면 개수만큼 answer에 더하고 pop
내 개수를 해당 개수 +1로 만듦
스택에 남은 값이 있다면 1을 더함
'''