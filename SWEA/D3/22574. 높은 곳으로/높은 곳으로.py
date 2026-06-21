TC = int(input())
for tc in range(1, TC+1):
    N, P = map(int, input().split())
    floor = 0
    for i in range(1, N+1):
        floor += i
        if floor == P:
            floor -= 1
    
    print(floor)