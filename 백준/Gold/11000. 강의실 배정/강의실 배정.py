import sys
import heapq
input = sys.stdin.readline

N = int(input())

time = [tuple(map(int, input().split())) for _ in range(N)]
time.sort()

pq = []
for s, e in time:
    if pq and pq[0]<=s:
        heapq.heappop(pq)
    heapq.heappush(pq, e)

print(len(pq))