import sys
input = sys.stdin.readline

def init_tree(node, s, e):
    if s == e:
        if s>M:
            segment_tree[node] = 1
        return
    
    mid = (s+e)//2
    init_tree(node*2, s, mid)
    init_tree(node*2+1, mid+1, e)
    segment_tree[node] = segment_tree[node*2] + segment_tree[node*2+1]

def update(node, s, e, idx, value):
    if idx<s or idx>e:
        return
    if s == e:
        segment_tree[node] = value
        return

    mid = (s+e)//2
    update(node*2, s, mid, idx, value)
    update(node*2+1, mid+1, e, idx, value)
    segment_tree[node] = segment_tree[node*2] + segment_tree[node*2+1]

def query(node, s, e, left, right):
    if e<left or s>right:
        return 0
    if left <= s and e <= right:
        return segment_tree[node]
    
    mid = (s+e)//2
    L = query(node*2, s, mid, left, right)
    R = query(node*2+1, mid+1, e, left, right)
    return L+R

    
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    K = N+M
    H = K.bit_length()
    segment_tree = [0]*(1<<(H+1))
    pos = [0]*(N+1)
    for i in range(1, N+1):
        pos[i] = i+M
    
    top = M
    init_tree(1, 1, K)
    answer = []
    for num in arr:
        idx = pos[num]
        answer.append(query(1, 1, K, 1, idx-1))
        update(1, 1, K, idx, 0)
        update(1, 1, K, top, 1)
        pos[num] = top
        top -= 1
   
    print(*answer) 


'''
해당 위치에 있는지 없는지 1,0으로 표시
pos[i] = i번 DVD의 트리에서 위치를 기록
update를 2번 호출(DVD빼기, 위로올리기)
query는 1~내 위치 직전까지
'''
