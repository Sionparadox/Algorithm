import sys
import heapq
input = sys.stdin.readline

N = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(N)]

lectures.sort(key= lambda x:x[1])
answer = [0]*(N+1)

pq = []
cnt = 0
for n, s, e in lectures:
    if pq and s>=pq[0][0]:
        et, rn = heapq.heappop(pq)
        answer[n] = rn
        heapq.heappush(pq, (e, rn))
    else:
        cnt += 1
        answer[n] = cnt
        heapq.heappush(pq, (e, cnt))

print(cnt)
for i in range(1, N+1):
    print(answer[i])


'''
시작 시간 기준으로 sort
pq는 끝나는 시간이 빠른 기준으로 우선순위
방 개수를 추적하며 pq에 새로운 방일때는 방개수를 추가해서 번호부여. 
있는 방에 넣을 때는 기존 번호 부여
'''
