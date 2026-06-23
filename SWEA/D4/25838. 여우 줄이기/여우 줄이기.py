TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    S = input()
    stack = []
    for c in S:
        if c == 'x' and len(stack) >= 2 and stack[-1] == 'o' and stack[-2] == 'f':
            stack.pop()
            stack.pop()
        else:
            stack.append(c)
    
    print(len(stack))