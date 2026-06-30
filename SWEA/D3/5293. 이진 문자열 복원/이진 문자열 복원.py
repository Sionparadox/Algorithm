TC = int(input())
for tc in range(1, TC+1):
    A, B, C, D = map(int, input().split())
    answer = 'impossible'
    
    zero = '0'*(A+1)
    one = '1'*(D+1)
    if B == 0 and C == 0:
        if A>0 and D == 0:
            answer = zero
        elif D>0 and A == 0:
            answer = one
    elif abs(B-C)<2:
        if C>B:
            answer = one + '01'*B + zero
        elif B>C:
            answer = zero + '10'*C + one
        else:
            answer = zero + one + '0' + '10'*(B-1)
    
    print(f'#{tc} {answer}')