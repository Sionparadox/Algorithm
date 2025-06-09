import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    s, e = map(int, input().split())
    graph[s].append(e)

labels = [0]*(V+1)
parent = [0]*(V+1)
isFinish = [False]*(V+1)
stack = []
answer = []
label = 0
def dfs(node):
    global label
    label += 1
    labels[node] = parent[node] = label
    stack.append(node)
    
    for next in graph[node]:
        # 처음 방문하는 노드
        if labels[next] == 0:
            dfs(next)
            parent[node] = min(parent[node], parent[next])
        # 방문했지만 끝나지않은(사이클인) 노드
        elif not isFinish[next]:
            parent[node] = min(parent[node], parent[next])
    
    if parent[node] == labels[node]:
        temp = []
        while True:
            v = stack.pop()
            temp.append(v)
            isFinish[v] = True
            if v == node:
                answer.append(sorted(temp))
                break

for i in range(1,  V+1):
    if not isFinish[i]:
        dfs(i)

print(len(answer))
answer.sort()
for arr in answer:
    print(' '.join(map(str, arr+[-1])))
