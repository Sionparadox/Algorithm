TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    while N % 2 == 0:
        N //= 2
    print(f"#{tc} {1 if N%4 == 3 else 0}")