import sys
input = sys.stdin.readline

def init_tree(node, s, e):
    if s == e:
        segment_tree[node] = nums[s]
        return
    
    mid = (s+e)//2
    init_tree(node*2, s, mid)
    init_tree(node*2+1, mid+1, e)
    segment_tree[node] = min(segment_tree[node*2], segment_tree[node*2+1])

def query(node, s, e, left, right):
    if right<s or left>e:
        return float('inf')
    if left <= s and e <= right:
        return segment_tree[node]
        
    mid = (s+e)//2
    L = query(node*2, s, mid, left, right)
    R = query(node*2+1, mid+1, e, left, right)
    return min(L, R)
    

N, M = map(int, input().split())
segment_tree = [0]*(4*N)
nums = [int(input()) for _ in range(N)]
init_tree(1, 0, N-1)
for _ in range(M):
    a, b = map(int, input().split())
    print(query(1, 0, N-1, a-1, b-1))