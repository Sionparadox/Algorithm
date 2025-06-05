import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

segmentTree = [(0,0)]*(N*4)


def merge(left, right):
    res = (0,0)
    if left[0] == right[0]:
        res = (left[0], min(left[1], right[1]))
    elif left[0] < right[0]:
        res = left
    else:
        res = right
    return res
        

def initTree(node=1, s=0, e=N-1):
    if s == e:
        segmentTree[node] = (nums[s], s)
    else :
        mid = (s+e)//2
        initTree(node*2, s, mid)
        initTree(node*2+1, mid+1, e)
        segmentTree[node] = merge(segmentTree[node*2], segmentTree[node*2+1])
            
def pick(left, right, node=1, s=0, e=N-1):
    if left > e or right < s:
        return (float('inf'), -1)
    if left <= s and e <= right:
        return segmentTree[node]
    
    mid = (s+e)//2
    return merge(pick(left, right, node*2, s, mid), pick(left, right, node*2+1, mid+1, e))
    
def update(idx, value, node=1, s=0, e=N-1):
    if idx<s or idx > e:
        return
    
    if s == e:
        segmentTree[node] = (value, idx)
        return
    
    mid = (s+e)//2
    update(idx, value, node*2, s, mid)
    update(idx, value, node*2+1, mid+1, e)
    segmentTree[node] = merge(segmentTree[node*2],segmentTree[node*2+1])


initTree()
M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b-1, c)
        nums[b-1] = c
    else:
        _, idx = pick(b-1, c-1)
        print(idx+1)