def update(idx, value):
    while idx <= N:
        fenwick_tree[idx] += value
        idx += idx & -idx
    

def query(idx):
    res = 0
    while idx > 0:
        res += fenwick_tree[idx]
        idx -= idx & -idx
    return res

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    nums = list(map(int, input().split()))
    fenwick_tree = [0]*(N+1)
    answer = 0
    for n in nums[::-1]:
        answer += query(n)
        update(n, 1)
    
    print(f'#{tc} {answer}')