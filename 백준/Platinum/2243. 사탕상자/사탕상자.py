import sys
input = sys.stdin.readline
MAX_VAL = 1000000

segmentTree = [0]*4*MAX_VAL
def update(value, cnt, node=1, s=1, e=MAX_VAL):
    if value<s or value>e:
        return
    segmentTree[node] += cnt
    if s == e:
        return
    
    mid = (s+e)//2
    update(value, cnt, node*2, s, mid)
    update(value, cnt, node*2+1, mid+1, e)

def pick(k, node=1, s=1, e=MAX_VAL):
    if s == e:
        update(s, -1)
        return s
    mid = (s+e)//2
    if segmentTree[node*2] >= k:
        return pick(k, node*2, s, mid)
    else :
        return pick(k-segmentTree[node*2], node*2+1, mid+1, e)


N = int(input())
for _ in range(N):
    order = list(map(int, input().split()))
    if order[0] == 1:
        print(pick(order[1]))
        
    else :
        update(order[1], order[2])

'''
세그먼트 트리로 해결
구간에 해당하는 개수를 저장하는 세그먼트 트리
리프노드에는 해당 노드에 해당하는 개수가 저장되어있음.

'''