import math
T = int(input())
for t in range(1, T+1):
    N, E, k = map(float, input().split())
    res = math.ceil(math.log(E/N, k))
    print(f'#{t} {res}')