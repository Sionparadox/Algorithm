TC = int(input())
for tc in range(1, TC+1):
    S = input()
    L = len(S)
    answer = 'Exist'
    for i in range(L//2):
        if S[i] != S[L-i-1] and S[i] != '*' and S[L-i-1] != '*':
            answer = 'Not exist'
        if S[i] == '*' or S[L-i-1] == '*':
            break
    
    print(f'#{tc} {answer}')