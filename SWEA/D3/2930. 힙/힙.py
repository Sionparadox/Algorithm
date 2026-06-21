import heapq

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    pq = []
    res = []
    for _ in range(N):
        cmd = input().split()
        if cmd[0] == '1':
            heapq.heappush(pq, (-int(cmd[1])))
        else:
            if pq:
                res.append(-heapq.heappop(pq))
            else:
                res.append(-1)
    
    print(f'#{tc}', *res)