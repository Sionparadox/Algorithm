import sys
MOD = 1000000007
input = sys.stdin.readline

N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

segmentTree = [1]*(N*4)

def initTree(node, s, e):
    if s == e:
        segmentTree[node] = nums[s]
    else :
        mid = (s+e)//2
        initTree(node*2, s, mid)
        initTree(node*2+1, mid+1, e)
        segmentTree[node] = segmentTree[node*2]*segmentTree[node*2+1]%MOD

def rangeMul(node, s, e, left, right):
    if left > e or right < s:
        return 1;
    if left <= s and e <= right:
        return segmentTree[node]
    mid = (s+e)//2
    return rangeMul(node*2, s, mid, left, right)*rangeMul(node*2+1, mid+1, e, left, right)%MOD

def update(node, s, e, idx, value):
    if idx < s or idx > e:
        return
    if s == e:
        segmentTree[node] = value
        return 
        
    mid = (s+e)//2
    update(node*2, s, mid, idx, value)
    update(node*2+1, mid+1, e, idx, value)
    segmentTree[node] = segmentTree[node*2] * segmentTree[node*2+1]%MOD

initTree(1, 0, N-1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0 ,N-1, b-1, c)
        nums[b-1] = c
    else :
        print(rangeMul(1, 0, N-1, b-1, c-1))
        