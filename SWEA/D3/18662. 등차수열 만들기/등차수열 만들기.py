TC = int(input())
for tc in range(1, TC+1):
    a, b, c = map(int, input().split())
    answer = min(abs(2*b-a-c), abs(a+c-2*b), abs((a+c)/2-b))
    print(f'#{tc} {answer:.1f}')