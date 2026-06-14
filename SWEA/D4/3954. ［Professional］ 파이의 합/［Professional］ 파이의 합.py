MAX = 1_000_000
pi = list(range(MAX+1))
for i in range(2, MAX + 1):
    if pi[i] == i:
        for j in range(i, MAX + 1, i):
            pi[j] -= pi[j] // i

prefix_sum = [0] * (MAX + 1)
for i in range(1, MAX + 1):
    prefix_sum[i] = prefix_sum[i - 1] + pi[i]
    
TC = int(input())
for tc in range(1, TC+1):
    a, b = map(int, input().split())
    print(f"#{tc} {prefix_sum[b]-prefix_sum[a-1]}")