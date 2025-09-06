import sys
input = sys.stdin.readline

N = int(input())
mapper = {}
_input = list(map(int, input().split()))
for i in range(N):
    mapper[_input[i]] = i

arr = [mapper[x] for x in list(map(int, input().split()))]
segment_tree = [0]*(4*N)

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
    if idx < s or idx > e:
        return
    if s == e:
        segment_tree[node] = value
        return
    
    mid = (s+e)//2
    update(node*2, s, mid, idx, value)
    update(node*2+1, mid+1, e, idx, value)
    segment_tree[node] = segment_tree[node*2]+segment_tree[node*2+1]


answer = 0
for k in arr:
    answer += query(1, 0, N-1, k+1, N-1)

    update(1, 0, N-1, k, 1)        
    
print(answer)


'''
i 가 들어왔을 때 이미 있는 i보다 큰 개수를 세기
세그먼트 트리로 logN
'''