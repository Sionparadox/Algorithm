TC = int(input())
for _ in range(TC):
    S = input()
    K = int(input())
    op = sum(map(int, input().split())) % len(S)
    print(S[op:]+S[:op])