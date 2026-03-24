import sys, heapq
input = sys.stdin.readline

N = int(input())
pq = []
for _ in range(N):
    d, v = map(int, input().split())
    heapq.heappush(pq, (-v, d))

time_parent = {0:0}
def find(t):
    if t not in time_parent:
        time_parent[t] = t
        return t
    if t == time_parent[t]:
        return t
    time_parent[t] = find(time_parent[t])
    return time_parent[t]

def union(u, v):
    u, v = find(u), find(v)
    time_parent[u] = v

answer = 0


while pq:
    value, deadline = heapq.heappop(pq)
    value = -value
    
    t = find(deadline)
    if t > 0:
        union(t, t-1)
        answer += value
    
print(answer)
    

'''
2,2,3,3 으로 데드라인이 있어도 3,3을 선택하는것이 최적일 수 있음.
-> value기반으로 우선순위
'''
