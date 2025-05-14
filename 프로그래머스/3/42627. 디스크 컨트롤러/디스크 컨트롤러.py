import heapq
def solution(jobs):
    jobs.sort()
    answer = 0
    pq = []
    time = 0
    idx = 0
    cnt = 0
    while cnt<len(jobs):
        while idx < len(jobs) and jobs[idx][0]<=time:
            heapq.heappush(pq, (jobs[idx][1], jobs[idx][0], idx))
            idx+=1
        if pq:
            length, start, i = heapq.heappop(pq)
            time += length
            answer += time-start
            cnt += 1
        else :
            time = jobs[idx][0]
        
    return answer//len(jobs)
