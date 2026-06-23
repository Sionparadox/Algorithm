TC = int(input())
for tc in range(1, TC+1):
    A, B, C, D = map(int, input().split())
    print(f'#{tc} {max(min(B, D) - max(A, C), 0)}')