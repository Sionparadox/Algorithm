import heapq
def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
    
    pq = []
    for idx, val in enumerate(food_times):
        heapq.heappush(pq, (val, idx+1))
    
    L = len(food_times)
    prev = 0
    while pq:
        time, _ = pq[0]
        diff = time - prev
        if diff == 0:
            heapq.heappop(pq)
            L -= 1
            continue

        if k < diff*L:
            res = sorted(pq, key=lambda x:x[1])
            return res[k%L][1]
        
        k -= diff*L
        prev = time
        heapq.heappop(pq)
        L -= 1
    
    return -1