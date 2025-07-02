import sys
input = sys.stdin.readline

toNum = {}

N = int(input())
postorder = input().strip()

for i in range(N):
    toNum[chr(i+65)] = int(input())

def calc(x, y, op):
    if op == '+':
        return x+y
    if op == '-':
        return x-y
    if op == '*':
        return x*y
    if op == '/':
        return x/y

stack = []
for c in postorder:
    if c.isalpha():
        stack.append(toNum[c])
        continue
    
    n2, n1 = stack.pop(), stack.pop()
    res = calc(n1, n2, c)
    stack.append(res)

print(f'{stack[0]:.2f}')
        