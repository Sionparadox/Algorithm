import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

ants = [int(input()) for _ in range(N)]
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    graph[a].append((b, c))
    graph[b].append((a, c))
K = 0
while (1<<K)<N:
    K += 1

arr = [[-1]*N for _ in range(K)]
energy = [[0]*N for _ in range(K)]

def make_tree(node, parent):
    for child, w in graph[node]:
        if child != parent:
            arr[0][child] = node
            energy[0][child] = w
            make_tree(child, node)
    
make_tree(0, -1)

for k in range(1, K):
    for i in range(N):
        if arr[k-1][i] == -1: continue
        arr[k][i] = arr[k-1][arr[k-1][i]]
        energy[k][i] = energy[k-1][i] + energy[k-1][arr[k-1][i]]

def move(node):
    if node == 0:
        return 0
    
    left = ants[node]
    for i in range(K-1, -1, -1):
        if arr[i][node] == -1:
            continue
        if left >= energy[i][node]:
            left -= energy[i][node]
            node = arr[i][node]
            if node == 0:
                break

    return node

for i in range(N):
    ant = move(i)
    print(ant+1)