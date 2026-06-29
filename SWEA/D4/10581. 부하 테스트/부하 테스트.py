import math
TC = int(input())
for tc in range(1, TC+1):
    L, P, C = map(int, input().split())
    K = math.ceil(math.log(P/L, C))
    print(f"#{tc} {math.ceil(math.log(K, 2))}")