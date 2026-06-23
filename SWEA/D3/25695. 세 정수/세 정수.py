TC = int(input())
for _ in range(TC):
    X, Y, Z = map(int, input().split())
    if X == Y and X>=Z:
        print(Z, Y, Z)
    elif Y == Z and Y >= X:
        print(X, X, Y)
    elif Z == X and Z >= Y:
        print(X, Y, Y)
    else:
        print(-1, -1, -1)