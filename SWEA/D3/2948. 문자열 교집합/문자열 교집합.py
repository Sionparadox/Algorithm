TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    A = set(input().split())
    B = set(input().split())
    print(f'#{tc} {len(A&B)}')