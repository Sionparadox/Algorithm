import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M = map(int, input().split())
if N<=2:
    print(-1)
    exit(0)

parent = [x for x in range(N+1)]

def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    rootU = find(u)
    rootV = find(v)
    if rootU != rootV:
        parent[rootV] = rootU

graph = defaultdict(list)
for i in range(1, M+1):
    u, v = map(int, input().split())
    graph[u].append((v, i))
    graph[v].append((u, i))

visited = [False]*(N+1)
queue = deque()
trees = []
degree = [0]*(N+1)
for node in range(1, N+1):
    if visited[node]:
        continue
    visited[node] = True
    tree = []
    queue = deque([node])
    while queue:
        now = queue.popleft()
        for nxt, num in graph[now]:
            if not visited[nxt]:
                union(now, nxt)
                visited[nxt] = True
                tree.append(num)
                queue.append(nxt)
                degree[now] += 1
                degree[nxt] += 1
    trees.append(tree)


L = len(trees)
if L>2:
    print(-1)
    exit(0)



if L==2: 
    if len(trees[0]) == len(trees[1]):
        print(-1)
        exit(0)
    else:
        roots = set(find(i) for i in range(1, N+1))
        root_list = sorted(list(roots))

        tree_nodes = {root: [] for root in roots}
        for i in range(1, N+1):
            tree_nodes[find(i)].append(i)
        R1, R2 = root_list[0], root_list[1]
        L1, L2 = trees[0], trees[1]
        N1, N2 = tree_nodes[R1], tree_nodes[R2]
        print(len(N1), len(N2))
        print(' '.join(map(str, N1)))
        print(' '.join(map(str, L1)))
        print(' '.join(map(str, N2)))
        print(' '.join(map(str, L2)))
        exit(0)

for leaf in range(1, N+1):
    if degree[leaf] == 1:
        break

def removeLine(node):
    lines = graph[node]
    target = set(trees[0])
    for line in lines:
        if line[1] in target:
            target.remove(line[1])
    return sorted(list(target))

line = removeLine(leaf)
print(N-1, 1)
print(' '.join([str(x) for x in range(1, N+1) if x != leaf]))
print(' '.join(map(str, line)))
print(leaf)
print()

'''
모든 정점을 잇는 아무 트리를 하나 만듦.(스패닝트리)
N<=2일 경우 -1
트리가 3개 이상이면 -1
트리가 2개일 때 정점의 개수가 같으면 -1
트리가 2개일 때는 그대로 2개 출력하면 답

트리의 리프노드 중 아무거나 선택해서 해당 노드를 분리,
이후 해당 노드와 연결된 모든 간선 제거
-> 분리 완료 (N-1크기의 트리와 1크기의 트리)

'''