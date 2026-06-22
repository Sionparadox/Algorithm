TC = int(input())
for _ in range(TC):
    B, W, X, Y, Z = map(int, input().split())
    answer = 0
    if B>W:
        answer += (B-W)*X
    else:
        answer += (W-B)*Y
    K = min(B, W)
    answer += max((X+Y)*K, 2*K*Z)
    print(answer)