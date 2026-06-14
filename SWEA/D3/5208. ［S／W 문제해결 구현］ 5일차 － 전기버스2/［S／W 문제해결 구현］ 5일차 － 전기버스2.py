from collections import deque
INF = float('inf')
TC = int(input())
for tc in range(1, TC+1):
    arr = list(map(int, input().split()))
    L = arr[0]
    dp = [INF]*(L+1)
    queue = deque([1])
    dp[1] = -1
    while queue:
        curr = queue.popleft()
        if curr == L:
            break
        for nxt in range(curr+1, curr+arr[curr]+1):
            if nxt>L:
                break
            if dp[nxt] != INF:
                continue
            dp[nxt] = dp[curr]+1
            queue.append(nxt)
    
    print(f'#{tc} {dp[L]}')