import heapq
TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    selected = list(map(int, input().split()))
    time = list(map(int, input().split()))
    member = [0]*(K+1)
    pq = []
    for i in range(N):
        member[selected[i]] += 1
        heapq.heappush(pq, (time[i], i, selected[i]))
    
    cnt = 0
    for m in member[1:]:
        if m == 0:
            cnt += 1
    
    answer = 0
    while pq and cnt>0:
        t, curr, task = heapq.heappop(pq)
        if member[task] == 1:
            continue
        
        member[task] -= 1
        answer += t
        cnt -= 1
    
    print(f'#{tc} {answer}')