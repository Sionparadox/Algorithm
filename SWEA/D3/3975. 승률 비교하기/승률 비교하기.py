TC = int(input())
answer = []
for tc in range(1, TC+1):
    A, B, C, D = map(int, input().split())
    x, y = A*D, B*C
    if x == y:
        answer.append(f'#{tc} DRAW')
    elif x > y:
        answer.append(f'#{tc} ALICE')
    else:
        answer.append(f'#{tc} BOB')
    
print('\n'.join(answer))