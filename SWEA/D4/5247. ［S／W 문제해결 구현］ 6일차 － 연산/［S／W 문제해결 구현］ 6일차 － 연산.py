from collections import deque
INF = float('inf')
MAX = 1_000_000

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    dp = [INF]*(MAX+1)
    dp[N] = 0
    queue = deque([N])
    while queue:
        curr = queue.popleft()
        for nxt in [curr-1, curr+1, curr*2, curr-10]:
            if nxt < 0 or nxt > MAX:
                continue
            if dp[nxt] != INF:
                continue
            dp[nxt] = dp[curr]+1
            queue.append(nxt)
    
    print(f'#{tc} {dp[M]}')