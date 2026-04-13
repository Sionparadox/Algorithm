import sys
input = sys.stdin.readline

def init_tree(node, s, e):
    if s == e:
        segment_tree[node] = nums[s]
        return
    
    mid = (s+e)//2
    init_tree(node*2, s, mid)
    init_tree(node*2+1 , mid+1, e)
    segment_tree[node] = segment_tree[node*2] + segment_tree[node*2+1]

def query(node, s, e, left, right):
    if right < s or left > e:
        return 0
    if left <= s and e <= right: 
        return segment_tree[node]
    
    mid = (s+e)//2
    L = query(node*2, s, mid, left, right)
    R = query(node*2+1, mid+1, e, left, right)
    return L+R

def update(node, s, e, idx, value):
    if idx<s or idx>e:
        return
    
    if s == e:
        segment_tree[node] += value
        return
    
    mid = (s+e)//2
    update(node*2, s, mid, idx, value)
    update(node*2+1, mid+1, e, idx, value)
    segment_tree[node] = segment_tree[node*2] + segment_tree[node*2+1]
    
N, Q = map(int, input().split())
nums = list(map(int, input().split()))
segment_tree = [0]*(N*4)
init_tree(1, 0, N-1)
for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x>y:
        x, y = y, x
    print(query(1, 0, N-1, x-1, y-1))
    diff = b-nums[a-1]
    nums[a-1] = b
    update(1, 0, N-1, a-1, diff)
