import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)

G_sum = 0
D_sum = 0
visited = [False]*N
visited[0] = True
queue = deque([0])

while queue:
    node = queue.popleft()
    l = len(tree[node])
    if l >=3:
        G_sum += l*(l-1)*(l-2)//6
    
    for nxt in tree[node]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        queue.append(nxt)
        nl = len(tree[nxt])
        D_sum += (l-1)*(nl-1)

G_sum *= 3
if G_sum > D_sum:
    print('G')
elif G_sum < D_sum:
    print('D')
else:
    print('DUDUDUNGA')
'''
G-Tree의 수 : 정점이 3개 이상 연결된 노드에 대해 xC3의 합
D-Tree의 수 : 인접한 두 노드에 대해 (x-1)*(y-1) 의 합
1-2-3-4-5
      6
1234, 2345, 2346, 4

2-3-4-5
  1 6
2345,2346, 1345, 1346, 3, 4
'''