import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]

segmentTree = [(0,0)]*(N*4)

def initTree(node, s, e):
    if s == e:
        segmentTree[node] = (nums[s], nums[s])
    else :
        mid = (s+e)//2
        initTree(node*2, s, mid)
        initTree(node*2+1, mid+1, e)
        left = segmentTree[node*2]
        right = segmentTree[node*2+1]
        segmentTree[node] = (min(left[0], right[0]), max(left[1], right[1]))

def rangeVal(node, s, e, left, right):
    if left > e or right < s:
        return (float('inf'), -float('inf'))
    if left <= s and e <= right:
        return segmentTree[node]
    mid = (s+e)//2
    
    l = rangeVal(node*2, s, mid, left, right)
    r = rangeVal(node*2+1, mid+1, e, left, right)
    return (min(l[0], r[0]), max(l[1], r[1]))

initTree(1, 0, N-1)
for _ in range(M):
    u, v = map(int, input().split())
    value = rangeVal(1, 0, N-1, u-1, v-1)
    print(value[0], value[1])
