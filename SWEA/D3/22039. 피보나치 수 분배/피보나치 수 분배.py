TC = int(input())
for _ in range(TC):
    N = int(input())
    k = N//3
    if N%3 == 1:
        print('impossible')
    elif N%3 == 2:
        print('BA'+'BBA'*k)
    else:
        print('BBA'*k)