TC = int(input())
answer = []
for tc in range(1, TC+1):
    N = int(input())
    answer.append(f'#{tc} {(N-1)%9+1}')
print('\n'.join(answer))