TC = int(input())
for tc in range(1, TC+1):
    N = int(input())+1
    turn = 0
    while N>1:
        if turn:
            N = N//2
        else:
            N = (N+1)//2
        turn = 1-turn

    print(f"#{tc} {'Bob' if turn else 'Alice'}")