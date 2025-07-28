import sys
input = sys.stdin.readline

N = int(input())
exp = input().strip()

def calc(x, op, y):
    if op == '+':
        return x+y
    if op == '-':
        return x-y
    if op == '*':
        return x*y

op_visit = [False]*(N//2)
answer = float('-inf')

def solve():
    stack = [int(exp[0])]
    for i in range(2, N, 2):
        if op_visit[(i-1)//2]:
            val = calc(stack.pop(), exp[i-1], int(exp[i]))
            stack.append(val)
        else:
            stack.append(exp[i-1])
            stack.append(int(exp[i]))
    
    res = stack[0]
    for i in range(1, len(stack), 2):
        res = calc(res, stack[i], stack[i+1])
    return res
    
def backTrack(idx):
    global answer
    if idx == N:
        answer = max(answer, solve())
        return 
    
    op = exp[idx]
    backTrack(idx+2)
    if idx==1 or not op_visit[idx//2-1]:
        op_visit[idx//2] = True
        backTrack(idx+2)
        op_visit[idx//2] = False
    
backTrack(1)
print(answer)