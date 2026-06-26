def update(idx, diff):
    while idx <= N:
        fenwick_tree[idx] += diff
        idx += idx & -idx

def query(idx):
    res = 0
    while idx > 0:
        res += fenwick_tree[idx]
        idx -= idx & -idx
    return res

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    fenwick_tree = [0]*(N+1)
    for i in range(N):
        update(i+1, nums[i])
    answer = []
    for _ in range(M):
        cmd, x, y = map(int, input().split())
        if cmd == 1:
            update(x, y)
        else:
            answer.append(query(y)-query(x-1))
    print(f'#{tc}', *answer)