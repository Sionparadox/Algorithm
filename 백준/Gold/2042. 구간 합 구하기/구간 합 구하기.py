import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

segmentTree = [0]*(N*4)

def initTree(node, s, e):
    if s == e:
        segmentTree[node] = nums[s]
    else :
        mid = (s+e)//2
        initTree(node*2, s, mid)
        initTree(node*2+1, mid+1, e)
        segmentTree[node] = segmentTree[node*2] + segmentTree[node*2+1]


def rangeSum(node, s, e, left, right):
    if left > e or right < s:
        return 0
    if left <= s and e <= right:
        return segmentTree[node]
    
    mid = (s+e)//2
    return rangeSum(node*2, s, mid, left, right) + rangeSum(node*2+1, mid+1, e, left, right)

def update(node, s, e, idx, value):
    if e<idx or s>idx : 
        return 
    segmentTree[node] += value
    if s == e:
        return
    mid = (s+e)//2
    update(node*2, s, mid, idx, value)
    update(node*2+1, mid+1, e, idx, value)


initTree(1, 0, N-1)
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, N-1, b-1, c-nums[b-1])
        nums[b-1] = c
    else :
        print(rangeSum(1, 0, N-1, b-1, c-1))