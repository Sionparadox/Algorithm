import sys
input = sys.stdin.readline

C = int(input())
    
for _ in range(C):
    N, M = map(int, input().split())
    board = [input().strip() for _ in range(N)]
    broken = [0]*N
    for i in range(N):
        mask = 0
        for j in range(M):
            if board[i][j] == 'x':
                mask |= (1<<j)
        broken[i] = mask
    
    vaild_masks = [[] for _ in range(N)]
    for i in range(N):
        for mask in range(1<<M):
            if mask & (mask<<1) or mask & broken[i]:
                continue
            vaild_masks[i].append(mask)
    
    dp = [[-1]*(1<<M) for _ in range(N)]
    
    for mask in vaild_masks[0]:
        dp[0][mask] = mask.bit_count()
    
    for r in range(1, N):
        for mask in vaild_masks[r]:
            for prev in vaild_masks[r-1]:
                if prev<<1 & mask or prev>>1 & mask:
                    continue
                dp[r][mask] = max(dp[r][mask], dp[r-1][prev] + mask.bit_count())
                    
    
    print(max(dp[N-1]))
                
    

'''
dp[row][mask] : row행 mask위치에 앉았을 때 배치할 수 있는 최대값
이전 mask와 비교해야함 -> 10* 2^10 * 2^10
각 행별로 가능한 mask를 미리 구해두기.
'''