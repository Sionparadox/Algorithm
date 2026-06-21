def check(n, arr):
    arr[n] += 1
    if arr[n] >= 3:
        return True
    if n>1 and arr[n-2] and arr[n-1]:
        return True
    if n>0 and n<9 and arr[n-1] and arr[n+1]:
        return True
    if n<8 and arr[n+1] and arr[n+2]:
        return True
    return False
    
TC = int(input())
for tc in range(1, TC+1):
    cards = list(map(int, input().split()))
    A = [0]*10
    B = [0]*10
    turn = True
    answer = 0
    for card in cards:
        if turn:
            if check(card, A):
                answer = 1
                break
        else:
            if check(card, B):
               answer = 2
               break 
            
        turn = not turn
    
    print(f'#{tc} {answer}')