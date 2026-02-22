import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
deleted_node = int(input())

children = [[] for _ in range(N)]
roots = []

def count_leaf(n):
    if not children[n]:
        return 1
    res = 0
    for child in children[n]:
        res += count_leaf(child)
    return res

for i in range(N):
    parent = arr[i]
    if parent==-1:
        roots.append(i)
        continue
    if i != deleted_node:    
        children[parent].append(i)

answer = 0
for root in roots:
    if root == deleted_node:
        continue
    answer += count_leaf(root)

print(answer)

'''
node마다 children 배열로 자식을 기록.
노드 지우기는 부모의 children 배열에서 해당 노드를 지워버리기
'''