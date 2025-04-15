def Queen(row):
    global cnt
    if(row==N):
        cnt += 1
    else:
        for i in range(N):
            check[row] = i
            if(not isAttack(row)):
                Queen(row+1)

def isAttack(k):
    for i in range(k):
        if(check[i] == check[k] or abs(k-i) == abs(check[k] - check[i])):
            return True
    return False

N = int(input())
cnt = 0
check = [0 for _ in range(N)]
Queen(0)
print(cnt)