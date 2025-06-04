import sys
import heapq
input = sys.stdin.readline

N = int(input())
pos = []
for _ in range(N):
    s, e = map(int, input().split())
    if s>e:
        s,e = e,s
    pos.append((s,e))

D = int(input())

pos.sort(key=lambda x:x[1])

answer = 0
pq = []
for s, e in pos:
    heapq.heappush(pq, s)
    
    while pq and pq[0] < e-D:
        heapq.heappop(pq)
    answer = max(answer, len(pq))

print(answer)


'''
끝점 기준 정렬
이후 끝점을 기준으로 for문을 돌림
반복문에서는 s를 우선순위 큐에 넣고 
이번에 선택된 e에 대해서 범위 밖에 있는 s를 다 pop
결국 큐에 남아있는 s의 수가 현재 e기준 커버할 수 있는 노드의 수가 됨
'''