import sys
input = sys.stdin.readline

def init_tree(node, s, e):
    if s == e:
        segment_tree[node] = nums[s]
        return
    
    mid = (s+e)//2
    init_tree(node*2, s, mid)
    init_tree(node*2+1, mid+1, e)
    segment_tree[node] = segment_tree[node*2] + segment_tree[node*2+1]

def lazy_update(node, s, e):
    if lazy[node] != 0:
    
        segment_tree[node] += (e-s+1)*lazy[node]
        if s != e:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0


def update(node, s, e, left, right, value):
    lazy_update(node, s, e)
    if e<left or s>right:
        return
    
    if left <= s and e <= right:
        segment_tree[node] += (e-s+1)*value
        if s != e:
            lazy[node*2] += value
            lazy[node*2+1] += value
        return

    mid = (s+e)//2
    update(node*2, s, mid, left, right, value)
    update(node*2+1, mid+1, e, left, right, value)
    segment_tree[node] = segment_tree[node*2] + segment_tree[node*2+1]


def query(node, s, e, left, right):
    lazy_update(node, s, e)
    if e<left or s>right:
        return 0
    if s >= left and e <= right:
        return segment_tree[node]
    
    mid = (s+e)//2
    L = query(node*2, s, mid, left, right)
    R = query(node*2+1, mid+1, e, left, right)
    return L+R


N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
H = N.bit_length()
segment_tree = [0]*(1<<(H+1))
lazy = [0]*(1<<(H+1))
init_tree(1, 0, N-1)

for _ in range(M+K):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        update(1, 0, N-1, cmd[1]-1, cmd[2]-1, cmd[3])
    else:
        print(query(1, 0, N-1, cmd[1]-1, cmd[2]-1))

