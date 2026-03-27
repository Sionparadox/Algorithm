import sys
input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(f'Case {t}:')
    for i in range(1,7):
        if 0 < N-i < 7 and i<=N-i:
            print(f'({i},{N-i})')