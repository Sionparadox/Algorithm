T = int(input())
index = {'red':0, 'orange':1, 'yellow':2, 'green':3, 'blue':4, 'purple':5}

for _ in range(T):
    A, B = input().split()
    x, y = index[A], index[B]
    if x == y:
        print('E')
    elif (x+3)%6 == y:
        print('C')
    elif abs(x-y) == 1 or abs(x-y) == 5:
        print('A')
    else:
        print('X')