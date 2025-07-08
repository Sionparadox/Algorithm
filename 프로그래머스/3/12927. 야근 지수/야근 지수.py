import heapq
def solution(n, works):
    answer = 0
    pq = []
    for work in works:
        heapq.heappush(pq, (-work, work))
        
    i = 0
    while i<n and pq:
        i += 1
        _, left = heapq.heappop(pq)
        left -= 1
        if left == 0:
            continue
        heapq.heappush(pq, (-left, left))
    
    while pq:
        _, left = heapq.heappop(pq)
        answer += left**2
    return answer