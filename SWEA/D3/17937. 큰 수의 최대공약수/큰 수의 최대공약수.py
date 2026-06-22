TC = int(input())
for tc in range(1, TC+1):
    A, B = map(int, input().split())
    print(f'#{tc} {A if A == B else 1}')