T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    print(2 if A%2==1 and B%2==1 and C%2==1 else 1)