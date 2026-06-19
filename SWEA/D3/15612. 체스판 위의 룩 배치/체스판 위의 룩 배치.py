TC = int(input())
for tc in range(1 ,TC+1):
    board = [input() for _ in range(8)]
    check = [False]*8
    flag = True
    for row in board:
        if row.count('O') != 1:
            flag = False
            break
        for i in range(8):
            if row[i] == 'O':
                if check[i]:
                    flag = False
                    break
                check[i] = True
        if not flag:
            break
    print(f"#{tc} {'yes' if flag else 'no'}")