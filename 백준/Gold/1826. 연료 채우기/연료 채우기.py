import sys, heapq
input = sys.stdin.readline

N = int(input())
station = [tuple(map(int, input().split())) for _ in range(N)]
L, P = map(int, input().split())
station.sort()
station.append((L, 0))
pq = []

remain = P
curr = 0
cnt = 0
for pos, fuel in station:
    d = pos-curr
    if remain < d:
        while pq and remain < d:
            remain += -heapq.heappop(pq)
            cnt += 1
        if remain<d:
            cnt = -1
            break
    
    heapq.heappush(pq, -fuel)
    curr = pos
    remain -= d

print(cnt)


'''
주유소 최대 1,000,000개
연료를 우선순위 큐에 넣기(최대힙).
이후 현재 위치, 남은 연료 추적하며 한바퀴로 해결
'''