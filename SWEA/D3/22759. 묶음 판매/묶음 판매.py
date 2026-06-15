TC = int(input())
for _ in range(1, TC+1):
    L, R = map(int, input().split())
    print('yes' if L*2>=R+1 else 'no')