import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
tree = {}
for idx, employee in enumerate(arr):
    if idx == 0:
        continue
    tree.setdefault(employee, []).append(idx)

def DFS(node):
    if node not in tree:
        return 0
    times = []
    for child in tree[node]:
        times.append(DFS(child))
        
    times.sort(reverse=True)
    return max(t+i+1 for i, t in enumerate(times))

print(DFS(0))