T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1:
        print(0)
    elif N%2 == 0:
        print('8'*(N//2))
    else:
        print('4'+'8'*(N//2))